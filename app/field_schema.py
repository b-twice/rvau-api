from webargs import fields, validate

schema = {
	"League": {
		'id': fields.Int(),
		'league_type': fields.Str(),
		'league_year': fields.Int(),

		'league': fields.Str(),

		'unique': fields.Str() # sql condition
	},
	"Team": {
		'id': fields.Int(),
		'team_name': fields.Str(),

		'unique': fields.Str()
	},
	"LeaguePlayer" : {
		'id': fields.Int(),	
		'league_year': fields.Int(),
		'league_type': fields.Str(),
		'team_name': fields.Str(),
		'first_name': fields.Str(),
		'last_name': fields.Str(),
		'player_type': fields.Str(),

		'player_name': fields.Str(),
		'league': fields.Str(),

		'unique': fields.Str()
	},
	"Player": {
		'id': fields.Int(),
		'first_name': fields.Str(),
		'last_name': fields.Str(),
		'email': fields.Str(),

		'player_name': fields.Str(),

		'unique': fields.Str()
	},
	"Game": {
		'id': fields.Int(),
		'game_date': fields.Str(),
		'game_type': fields.Str(),
		'league_year': fields.Int(),
		'league_type': fields.Str(),
		'home_team': fields.Str(),
		'away_team': fields.Str(),
		'home_score': fields.Int(),
		'away_score': fields.Int(),


		'league': fields.Str(),
		'unique': fields.Str()
	},

}