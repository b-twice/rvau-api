DROP VIEW IF EXISTS LeaguePlayerView;
CREATE VIEW LeaguePlayerView AS
	SELECT 
		id, 
		(league_year || ' ' || league_type) AS league,
		team_name,
		(first_name || ' ' || last_name) AS player_name,
		player_type
	FROM LeaguePlayer;

DROP VIEW IF EXISTS LeagueView;
CREATE VIEW LeagueView AS
	SELECT 
		id, 
		league_year,
		league_type,
		(league_year || ' ' || league_type) AS league
	FROM League;



DROP VIEW IF EXISTS GameView;
CREATE VIEW GameView AS
	SELECT 
		id, 
		game_date,
		game_type,
		(league_year || ' ' || league_type) AS league,
		home_team,
		away_team,
		home_score,
		away_score
	FROM Game;