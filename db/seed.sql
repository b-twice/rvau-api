--Enable Cascade
pragma foreign_keys=on;
.separator ","
.import db/seed/Team.csv Team
.import db/seed/League.csv League
.import db/seed/Player.csv Player
.import db/seed/PlayerLeague.csv LeaguePlayer
.import db/seed/Game.csv Game