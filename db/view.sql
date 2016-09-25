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
		COUNT(CASE WHEN home_score > away_score AND game_type = "Final" THEN 1 END) as champion,
		SUM(home_score) - SUM(away_score) as point_diff				
	FROM GameView
	GROUP BY league, home_team;

SELECT "HOME SUMMARY";
SELECT * FROM HomeSummary;

DROP VIEW IF EXISTS AwaySummary;
CREATE VIEW AwaySummary AS
	SELECT 
		league,
		away_team as team_name,
		COUNT(CASE WHEN away_score > home_score AND game_type = "Season"  THEN 1 END) AS win_count,
		COUNT(CASE WHEN away_score < home_score AND game_type = "Season"  THEN 1 END) AS loss_count,
		COUNT(CASE WHEN away_score = home_score AND game_type = "Season"  THEN 1 END) AS tie_count,		
		COUNT(CASE WHEN away_score > home_score AND game_type = "Final" THEN 1 END) as champion,
		SUM(away_score) - SUM(home_score) as point_diff		
	FROM GameView
	GROUP BY league, away_team;

SELECT "AWAY SUMMARY";
SELECT * FROM AwaySummary;

DROP VIEW IF EXISTS LeagueSummaryView;
CREATE VIEW LeagueSummaryView AS
	SELECT 
		league,
		team_name,
		SUM(win_count) as win_count,
		SUM(loss_count) as loss_count,
		SUM(tie_count) as tie_count,
		SUM(champion) as champion,
		SUM(point_diff) as point_diff
		FROM (
			SELECT league, team_name, win_count, loss_count, tie_count, champion, point_diff
			FROM HomeSummary
			UNION ALL
			SELECT league, team_name, win_count, loss_count, tie_count, champion, point_diff
			FROM AwaySummary
			) 
		GROUP BY league, team_name;


SELECT "LEAGUE SUMMARY";
SELECT * FROM LeagueSummaryView ORDER BY win_count DESC, tie_count DESC;
