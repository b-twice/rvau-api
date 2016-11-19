fields = {
	"League": [
		'id',
		'league_type',
		'league_year'
	],
	"LeagueView": [
		'id',
		'league_type',
		'league_year',
		'league'
	],
	"Team": [
		'id',
		'team_name'
	],
	"LeaguePlayer": [
		'id',
		'league_type',
		'league_year',
		"team_name",
		"first_name",
		"last_name",
		"player_type"
	],
	"LeaguePlayerView": [
		'id',
		'league',
		"team_name",
		"player_name",
		"player_type"
	],
	"Player": [
		"id",
		"first_name",
		"last_name",
		"email"
	],
	"PlayerView": [
		"id",
		"first_name",
		"last_name",
		"email",
		"player_name"
	],
	"Game": [
		"id",
		"game_date",
		"game_type",
		"league_year",
		"league_type",
		"home_team",
		"away_team",
		"home_score",
		"away_score",
	],
	"GameView": [
		"id",
		"game_date",
		"game_type",
		"league",
		"home_team",
		"away_team",
		"home_score",
		"away_score",
	],
	"LeagueSummary":[
		"id",
		"league",
		"team_name",
		"win_count",
		"loss_count",
		"tie_count",
		"champion",
		"point_diff"
	]
}