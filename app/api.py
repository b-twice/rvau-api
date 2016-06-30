#!flask/bin/python
from app import app, api
from flask_restful import abort
from resources import *

class Routing(object):
    base = "/rvau/api/"

    leagues = "{}leagues".format(base)
    league = "{}leagues/<id>".format(base)

    teams = "{}teams".format(base)
    team = "{}teams/<id>".format(base)

    players = "{}players".format(base)
    player = "{}players/<id>".format(base)

    league_players = "{}leagueplayers".format(base)
    league_player = "{}leagueplayers/<id>".format(base)

    games = "{}games".format(base)
    game = "{}games/<id>".format(base)

 # This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)

api.add_resource(Leagues, Routing.leagues, endpoint="leagues")
api.add_resource(League, Routing.league, endpoint="league")

api.add_resource(Teams, Routing.teams, endpoint="teams")
api.add_resource(Team, Routing.team, endpoint="team")

api.add_resource(LeaguePlayers, Routing.league_players, endpoint="leagueplayers")
api.add_resource(LeaguePlayer, Routing.league_player, endpoint="leagueplayer")

api.add_resource(Players, Routing.players, endpoint="players")
api.add_resource(Player, Routing.player, endpoint="player")

api.add_resource(Games, Routing.games, endpoint="games")
api.add_resource(Game, Routing.game, endpoint="game")