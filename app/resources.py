from field_schema import schema
from flask_restful import Resource, abort
from db import *
from webargs.flaskparser import use_args, use_kwargs, parser


class BaseResource(Resource):
    def __init__(self):
        self.name = self.__class__.__name__
        self.arg_schema = schema[self.name]

    def query(self, name, args):
        select = "SELECT * FROM {}".format(name)
        where = create_where(name, args.keys()) if args else select
        result = query_db(where, args.values())
        if len(result) == 0:
            abort(404)
        return result

    def insert(self, name, args):
        statement = create_insert(name, args.keys())
        isPosted = insert_db(statement, args)
        if not isPosted:
            abort(500, errors={"message":"Data could not be posted"})
        return args

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

class LeaguePlayer(BaseResource):
    arg_schema = schema["LeaguePlayer"]
    @use_args(arg_schema)
    def get(self, args):
        result = self.query(self.name, args)
        return {"data": result}

    @use_args(arg_schema)
    def post(self, args):
        results = self.insert(self.name, args)
        return {"data": results}

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