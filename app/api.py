#!flask/bin/python
from app import app, api
from flask_restful import abort
from resources import *

class Routing(object):
    base = "/rvau/api/"
    leagues = "{}leagues".format(base)
    teams = "{}teams".format(base)
    players = "{}players".format(base)
    league_players = "{}leagueplayers".format(base)
    games = "{}games".format(base)


 # This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)

api.add_resource(League, Routing.leagues, endpoint="leagues")
api.add_resource(Team, Routing.teams, endpoint="teams")
api.add_resource(LeaguePlayer, Routing.league_players, endpoint="leagueplayers")
api.add_resource(Player, Routing.players, endpoint="players")
api.add_resource(Game, Routing.games, endpoint="games")