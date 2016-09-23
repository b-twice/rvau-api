from webargs import fields, validate
from collections import OrderedDict

schema = {
	"League": OrderedDict([
		('id', fields.Int()),
		('league_type', fields.Str()),
		('league_year', fields.Int()),

		# view params
		('league', fields.Str()),

		# optional params
		('unique', fields.Str()), 
		('exclude',fields.Str())
	]),
	"Team": OrderedDict([
		('id', fields.Int()),
		('team_name', fields.Str()),

		# optional params
		('unique', fields.Str()), 
		('exclude',fields.Str())
	]),
	"LeaguePlayer": {
		'id': fields.Int(),	
		'league_year': fields.Int(),
		'league_type': fields.Str(),
		'team_name': fields.Str(),
		'first_name': fields.Str(),
		'last_name': fields.Str(),
		'player_type': fields.Str(),

		# concat view params
		'player_name': fields.Str(),
		'league': fields.Str(),

		# optional params
		'unique': fields.Str(), 
		'exclude':fields.Str()
	},
	"Player": OrderedDict([
		('id', fields.Int()),
		('first_name', fields.Str()),
		('last_name', fields.Str()),
		('email', fields.Str()),
		('player_name', fields.Str()),

		# optional params
		('unique', fields.Str()), 
		('exclude',fields.Str())

	]),
	"Game": OrderedDict([
		('id', fields.Int()),
		('game_date', fields.Str()),
		('game_type', fields.Str()),
		('league_year', fields.Int()),
		('league_type', fields.Str()),
		('home_team', fields.Str()),
		('away_team', fields.Str()),
		('home_score', fields.Int()),
		('away_score', fields.Int()),

		# concat view params
		('league', fields.Str()),

		# optional params
		('unique', fields.Str()), 
		('exclude',fields.Str())

	]),
	"LeagueSummary": OrderedDict([
		('id', fields.Int()),
		('league', fields.Str()),
		('team_name', fields.Str()),
		('win_count', fields.Int()),
		('loss_count', fields.Int()),
		('tie_count', fields.Int()),
		('champion', fields.Int()),

		# optional params
		('unique', fields.Str()),		
		('exclude',fields.Str())		
	])
}