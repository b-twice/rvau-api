from field_schema import schema
from flask_restful import Resource, abort
from db import *
from webargs.flaskparser import use_args, use_kwargs, parser


class BaseResource(Resource):

    def query(self, name, args):
        select = "SELECT * FROM {}".format(name)
        where = "{} {}".format(select, create_where(name, args.keys())) if args else select
        print where
        print select
        result = query_db(where, args.values())
        if len(result) == 0:
            abort(404)
            return
        return result

    def insert(self, name, args):
        statement = create_insert(name, args.keys())
        isPosted = modify_db(statement, args)
        if not isPosted:
            abort(500)
            return
        return args

    def update(self, name, args):
        statement = create_update(name, args.keys())
        isUpdated = modify_db(statement, args)
        if not isUpdated:
            abort(500)
            return
        return args

    def delete(self, name, args):
        statement = "DELETE * FROM {} WHERE id=:id".format(name)
        isDelete = modify_db(statement, args)
        if not isDelete:
            abort(500)
            return
        return args

class Leagues(BaseResource):
    arg_schema = schema["League"]
    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

class League(BaseResource):
    arg_schema = schema["League"]   

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def put(self, args):
        results = self.update(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def delete(self, args):
        results = self.delete(self.name, args)
        return 

class Teams(BaseResource):
    arg_schema = schema["Team"]
    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

class Team(BaseResource):
    arg_schema = schema["Team"]

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def put(self, args):
        results = self.update(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def delete(self, args):
        results = self.delete(self.name, args)
        return 

class Players(BaseResource):
    arg_schema = schema["Player"]
    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

class Player(BaseResource):
    arg_schema = schema["Player"]

    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def put(self, args):
        results = self.update(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def delete(self, args):
        results = self.delete(self.name, args)
        return 

class LeaguePlayers(BaseResource):
    arg_schema = schema["LeaguePlayer"]
    def __init__(self):
        self.name = "LeaguePlayer"

    @use_args(arg_schema)
    def get(self, args):
        print "hello"
        result = self.query(self.name, args)
        return {"data": result}

class LeaguePlayer(BaseResource):
    arg_schema = schema["LeaguePlayer"]
    def __init__(self):
        self.name = "LeaguePlayer"

    def get(self, id):
        print "hi"
        result = self.query(self.name, {"id":id})
        return {"data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def put(self, args):
        results = self.update(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def delete(self, args):
        results = self.delete(self.name, args)
        return 

class Games(BaseResource):
    arg_schema = schema["Game"]
    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

class Game(BaseResource):
    arg_schema = schema["Game"]
    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def put(self, args):
        results = self.update(self.name, args)
        return {"data": results}

    @use_args(arg_schema)
    def delete(self, args):
        results = self.delete(self.name, args)
        return 