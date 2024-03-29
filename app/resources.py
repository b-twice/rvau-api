from field_schema import schema
from field_map import fields
from flask_restful import Resource, abort
from webargs.flaskparser import use_args, use_kwargs, parser
from db import *
from authentication import authenticate


class BaseResource(Resource):

    def __init__(self):
        self.query_params = ['unique', 'exclude']

    def decompose(self, args):
        if 'league' in args:
            args["league_year"] = args['league'].split(' ')[0]
            args["league_type"] = args['league'].split(' ')[1]
            args.pop('league')
        if 'player_name' in args:
            args["first_name"] = args['player_name'].split(' ')[0]
            args["last_name"] = args['player_name'].split(' ')[1]
            args.pop('player_name')

    def cleanup_args(self, args):
        args.pop('unique', None)
        args.pop('exclude', None)
        args.pop('ASC', None)
        args.pop('DESC', None)

    def query(self, name, args):
        columns = []
        # get all unique values in a specific column
        if 'unique' in args:
            columns = [args["unique"]]
            select = "SELECT {} FROM {} GROUP BY {}".format(args["unique"], name, args["unique"])
            self.cleanup_args(args)
        else:
            columns = fields[name]
            order = ""
            # Exclude removes any columns from query
            if 'ASC' in args or 'DESC' in args:
                asc_order_args = args['ASC'].split(',') if 'ASC' in args else [] 
                desc_order_args = args['DESC'].split(',') if 'DESC' in args else []                       
                order = create_order(asc_order_args, desc_order_args)    
            if 'exclude' in args:
                columns = [c for c in columns if c not in args['exclude'].split(',')]
            self.cleanup_args(args)
            select = "SELECT {} FROM {}".format(",".join(columns), name)
            where = create_where(name, args.keys())     
            select = "{} {} {}".format(select, where, order) if args else select
        result = query_db(select, args.values())
        if len(result) == 0:
            abort(404)
            return
        return result, columns

    def insert(self, name, args, view_name=""):
        statement = create_insert(name, args.keys())
        insertId = modify_db(statement, args)
        if insertId == False:
            abort(500, errors="Could not add the row. The row may already exist.")
            return
        # Get full result of query
        return self.query(view_name, {'id': insertId})[0] if view_name else self.query(name, {'id': insertId})[0]

    def update(self, name, args):
        statement = create_update(name, args.keys())
        isUpdated = modify_db(statement, args)
        if isUpdated == False:
            abort(500, errors="Could not update the record")
            return
        return args

    def deleteRecord(self, name, args):
        statement = "DELETE FROM {} WHERE id=:id".format(name)
        isDelete = modify_db(statement, args)
        if isDelete == False:
            abort(500, errors="Could not delete the record. Record may be in use by another table.")
            return
        return args

class Leagues(BaseResource):
    arg_schema = schema["League"]
    def __init__(self):
        self.name = "League"
        self.view_name = "LeagueView"
        self.alias = "leagues"

    @use_args(arg_schema)
    def get(self, args):
        result, columns = self.query(self.view_name, args)
        return {"table": self.alias, "data": result,  "keys":columns}

    @use_args(arg_schema)
    @authenticate 
    def post(self, args):
        results = self.insert(self.name, args)
        return {"table": self.alias, "data": results}


class League(BaseResource):     
    arg_schema = schema["League"]
    def __init__(self):
        self.name = "League"
        self.view_name = "LeagueView"
        self.alias = "leagues"

    def get(self, id):
        result, columns = self.query(self.view_name,  {"id":id})
        return {"table": self.alias, "data": result,  "keys":columns}

    @use_args(arg_schema)
    @authenticate  
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    @authenticate
    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class Teams(BaseResource):
    arg_schema = schema["Team"]
    def __init__(self):
        self.name = "Team"
        self.alias = "teams"

    @use_args(arg_schema)
    def get(self, args):
        result, columns = self.query(self.name, args)
        return {"table": self.alias, "data": result,  "keys":columns}
    
    @authenticate
    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"table": self.alias, "data": results}

class Team(BaseResource):
    arg_schema = schema["Team"]
    def __init__(self):
        self.name = "Team"
        self.alias = "teams"

    def get(self, id):
        result = self.query(self.name, {"id":id})
        return {"table": self.alias, "data": result,  "keys":schema["Team"].keys()}

    @use_args(arg_schema)
    @authenticate
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results,}

    @authenticate
    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class Players(BaseResource):
    arg_schema = schema["Player"]
    def __init__(self):
        self.name = "Player"
        self.view_name = "PlayerView"
        self.alias = "players"   

    @use_args(arg_schema)
    def get(self, args):
        result, columns = self.query(self.view_name, args)
        return {"table": self.alias, "data": result,  "keys":columns}

    @use_args(arg_schema)
    @authenticate
    def post(self, args):
        results = self.insert(self.name, args)
        return {"table": self.name, "data": results}

class Player(BaseResource):
    arg_schema = schema["Player"]
    def __init__(self):
        self.name = "Player"
        self.alias = "players"

    def get(self, id):
        result, columns = self.query(self.name, {"id":id})
        return {"table": self.alias, "data": result,  "keys":columns}

    @use_args(arg_schema)
    @authenticate
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    @authenticate
    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class LeaguePlayers(BaseResource):
    arg_schema = schema["LeaguePlayer"]
    def __init__(self):
        self.name = "LeaguePlayer"
        self.view_name = "LeaguePlayerView"
        self.alias = "leagueplayers"

    @use_args(arg_schema)
    def get(self, args):
        result, columns = self.query(self.view_name, args)
        return {"table": self.alias, "data": result, "keys":columns}

    @authenticate
    @use_args(arg_schema)
    def post(self, args):
        self.decompose(args)
        results = self.insert(self.name, args, self.view_name)
        return {"table": self.alias, "data": results}

class LeaguePlayer(BaseResource):
    arg_schema = schema["LeaguePlayer"]
    def __init__(self):
        self.name = "LeaguePlayer"
        self.view_name = "LeaguePlayerView"
        self.alias = "leagueplayers"

    def get(self, id):
        result, columns = self.query(self.view_name, {"id":id})
        return {"table": self.alias, "data": result, keys: columns}

    @use_args(arg_schema)
    @authenticate
    def put(self, args, id):
        args["id"] = id
        self.decompose(args)
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results}

    @authenticate
    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}

class Games(BaseResource):
    arg_schema = schema["Game"]

    def __init__(self):
        self.name = "Game"
        self.view_name = "GameView"
        self.alias = "games"

    @use_args(arg_schema)
    def get(self, args):
        result, columns = self.query(self.view_name, args)
        return {"table": self.alias, "data": result, "keys":columns}

    @use_args(arg_schema)
    @authenticate
    def post(self, args):
        print args
        results = self.insert(self.name, args)
        return {"table": self.alias, "data": results}


class Game(BaseResource):
    arg_schema = schema["Game"]

    def __init__(self):
        self.name = "Game"
        self.view_name = "GameView"
        self.alias = "games"

    def get(self, id):
        result, columns = self.query(self.view_name, {"id":id})
        return {"table": self.alias, "data": result, "keys":columns}

    @use_args(arg_schema)
    @authenticate
    def put(self, args, id):
        args["id"] = id
        results = self.update(self.name, args)
        return {"table": self.alias, "data": results, "keys":schema["Game"].keys()}

    @authenticate
    def delete(self, id):
        results = self.deleteRecord(self.name, {"id":id})
        return {"data": {"id":id}}


class LeagueSummary(BaseResource):
    arg_schema = schema["LeagueSummary"]
    
    def __init__(self):
        self.name = "LeagueSummary"
        self.alias = "leaguesummary"

    @use_args(arg_schema)
    def get(self, args):
        result, column = self.query(self.name, args)
        return {"table": self.alias, "data": result, "keys":column}
