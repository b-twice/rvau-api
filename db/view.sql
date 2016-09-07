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

DROP VIEW IF EXISTS PlayerView;
CREATE VIEW PlayerView AS
	SELECT 
		id, 
		first_name,
		last_name,
		email,
		(first_name || ' ' || last_name) AS player_name
	FROM Player;

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

DROP VIEW IF EXISTS HomeSummary;
CREATE VIEW HomeSummary AS
	SELECT 
		league,
		home_team as team_name,
		COUNT(CASE WHEN home_score > away_score AND game_type = "Season" THEN 1 END) AS win_count,
		COUNT(CASE WHEN home_score < away_score AND game_type = "Season"  THEN 1 END) AS loss_count,
		COUNT(CASE WHEN home_score = away_score AND game_type = "Season"  THEN 1 END) AS tie_count,
		COUNT(CASE WHEN home_score > away_score AND game_type = "Championship" THEN 1 END) as champion
	FROM GameView
	GROUP BY league, home_team;

DROP VIEW IF EXISTS AwaySummary;
CREATE VIEW AwaySummary AS
	SELECT 
		league,
		away_team as team_name,
		COUNT(CASE WHEN away_score > home_score AND game_type = "Season"  THEN 1 END) AS win_count,
		COUNT(CASE WHEN away_score < home_score AND game_type = "Season"  THEN 1 END) AS loss_count,
		COUNT(CASE WHEN away_score > home_score AND game_type = "Championship" THEN 1 END) as champion		
	FROM GameView
	GROUP BY league, away_team;

DROP VIEW IF EXISTS LeagueSummaryView;
CREATE VIEW LeagueSummaryView AS
	SELECT 
		HomeSummary.league,
		HomeSummary.team_name,
		HomeSummary.win_count + AwaySummary.win_count AS win_count,
		HomeSummary.loss_count + AwaySummary.loss_count AS loss_count,
		HomeSummary.tie_count,
		HomeSummary.champion + AwaySummary.champion AS champion	
	FROM HomeSummary
    INNER JOIN AwaySummary
    ON HomeSummary.league = AwaySummary.league AND HomeSummary.league = AwaySummary.league
	GROUP BY HomeSummary.league, HomeSummary.team_name;

