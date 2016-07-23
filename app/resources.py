from field_schema import schema
from flask_restful import Resource, abort
from webargs.flaskparser import use_args, use_kwargs, parser
from db import *
from authentication import authenticate


class BaseResource(Resource):

    def decompose(self, args):
        if 'league' in args:
            args["league_year"] = args['league'].split(' ')[0]
            args["league_type"] = args['league'].split(' ')[1]
            args.pop('league')
        if 'player_name' in args:
            args["first_name"] = args['player_name'].split(' ')[0]
            args["last_name"] = args['player_name'].split(' ')[1]
            args.pop('player_name')

    def query(self, name, args,):
        select = "SELECT * FROM {}".format(name)
        if 'unique' in args:
            select = "SELECT {} FROM {} GROUP BY {}".format(args["unique"], name, args["unique"])
            args.pop('unique', None)
        else:
             select = "{} {}".format(select, create_where(name, args.keys())) if args else select
        result = query_db(select, args.values())
        if len(result) == 0:
            abort(404)
            return
        return result

    def insert(self, name, args, view_name=""):
        statement = create_insert(name, args.keys())
        insertId = modify_db(statement, args)
        if not insertId:
            abort(500, errors="Could not add the row. The row may already exist.")
            return
        # Get full result of query
        return self.query(view_name, {'id': insertId})[0] if view_name else self.query(name, {'id': insertId})[0]

    def update(self, name, args):
        statement = create_update(name, args.keys())
        isUpdated = modify_db(statement, args)
        if not isUpdated:
            abort(500)
            return
        return args

    def deleteRecord(self, name, args):
        statement = "DELETE FROM {} WHERE id=:id".format(name)
        isDelete = modify_db(statement, args)
        if not isDelete:
            abort(500, errors="Could not delete record. Record may be in use by another table.")
            return
        return args

class Leagues(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["League"]
    def __init__(self):
        self.name = "League"
        self.view_name = "LeagueView"
        self.alias = "leagues"

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.view_name, args)
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"table": self.alias, "data": results}


class League(BaseResource):
    method_decorators = [authenticate]      
    arg_schema = schema["League"]
    def __init__(self):
        self.name = "League"
        self.view_name = "LeagueView"
        self.alias = "leagues"

    def get(self, id):
        result = self.query(self.view_name, {"id":id})
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class Teams(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["Team"]
    def __init__(self):
        self.name = "Team"
        self.alias = "teams"

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"table": self.alias, "data": results}

class Team(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["Team"]
    def __init__(self):
        self.name = "Team"
        self.alias = "teams"

    def get(self, id):
        result = self.query(self.name, {"id":id})
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class Players(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["Player"]
    def __init__(self):
        self.name = "Player"
        self.view_name = "PlayerView"
        self.alias = "players"   

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.view_name, args)
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"table": self.name, "data": results}

class Player(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["Player"]
    def __init__(self):
        self.name = "Player"
        self.alias = "players"

    def get(self, id):
        result = self.query(self.name, {"id":id})
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class LeaguePlayers(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["LeaguePlayer"]
    def __init__(self):
        self.name = "LeaguePlayer"
        self.view_name = "LeaguePlayerView"
        self.alias = "leagueplayers"

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.view_name, args)
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def post(self, args):
        self.decompose(args)
        results = self.insert(self.name, args, self.view_name)
        return {"table": self.alias, "data": results}

class LeaguePlayer(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["LeaguePlayer"]
    def __init__(self):
        self.name = "LeaguePlayer"
        self.view_name = "LeaguePlayerView"
        self.alias = "leagueplayers"

    def get(self, id):
        result = self.query(self.view_name, {"id":id})
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def put(self, args, id):
        args["id"] = id
        self.decompose(args)
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class Games(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["Game"]

    def __init__(self):
        self.name = "Game"
        self.view_name = "GameView"
        self.alias = "games"

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.view_name, args)
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def post(self, args):
        print args
        results = self.insert(self.name, args)
        return {"table": self.alias, "data": results}


class Game(BaseResource):
    method_decorators = [authenticate]
    arg_schema = schema["Game"]

    def __init__(self):
        self.name = "Game"
        self.view_name = "GameView"
        self.alias = "games"

    def get(self, id):
        result = self.query(self.view_name, {"id":id})
        return {"table": self.alias, "data": result}

    @use_args(arg_schema)
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}
