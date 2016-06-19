from webargs import fields, validate

schema = {
	"League": {
		'league_type': fields.Str(),
		'league_year': fields.Int()
	},
	"Team": {
		'team_name': fields.Str()
	},
	"LeaguePlayer" : {
		'league_year': fields.Int(),
		'league_type': fields.Str(),
		'team_name': fields.Str(),
		'player_first_name': fields.Str(),
		'player_last_name': fields.Str()
	},
	"Player": {
		'first_name': fields.Str(),
		'last_name': fields.Str(),
		'email': fields.Str()
	},
	"Game": {
		'game_date': fields.Str(),
		'game_type': fields.Str(),
		'league_year': fields.Int(),
		'league_type': fields.Str(),
		'home_team': fields.Str(),
		'away_team': fields.Str(),
		'home_score': fields.Int(),
		'away_score': fields.Int()
	}

}