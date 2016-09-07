INSERT OR REPLACE INTO LeagueSummary (league, team_name, win_count, loss_count, tie_count, champion)
    SELECT league, team_name, win_count, loss_count, tie_count, champion
    FROM LeagueSummaryView;

DROP VIEW IF EXISTS HomeSummary;
DROP VIEW IF EXISTS AwaySummary;
DROP VIEW IF EXISTS LeagueSummaryView;

SELECT * FROM LeagueSummary;