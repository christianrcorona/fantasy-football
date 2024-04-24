import football

#qb1 = football.Player("Josh Allen", "QB", "Buffalo Bills", {"passing_yards": 316, "passing_tds": 3, "rushing_yards": 15, "rushing_tds": 0, "interceptions": 1})
#qb2 = football.Player("Jalen Hurts", "QB", "Philidelphia Eagles", {"passing_yards": 466, "passing_tds": 1, "rushing_yards": 27, "rushing_tds": 1, "interceptions": 1})
#team1_rb1 = football.Player("Derek Henry", "RB", "Tennessee Titans", {"rushing_yards": 132, "total_carries": 14, "rushing_tds": 1, "receiving_yds": 48})
#team1_wr1 = football.Player("Tyreek Hill", "WR", "Miami Dolphins", {"receptions": 6, "receiving_yards": 215, "receiving_tds": 2, "rushing_yards": 0})
#team1_wr2 = football.Player("Stefon Diggs", "WR", "Buffalo Bills", {"receptions": 3, "receiving_yards": 102, "receiving_tds": 1, "rushing_yards": 0})
#team1_te1 = football.Player("Travis Kelce", "TE", "Kansas City Chiefs", {"receptions": 4, "receiving_yds": 55, "receiving_tds": 2})
#team1_defense = football.Player("Cowboys Defensive line", "Defense", "Dallas", {"yards_against": 157, "interceptions": 2, "points_allowed": 10})
#team1_kicker = football.Player("Justin Tucker", "Kicker", "Baltimore Ravens", {"FG_made": 2, "PAT_made": 4})
#team2_rb1 = football.Player("Breece Hall", "RB", "New York Jets", {"rushing_yards": 213, "total_carries": 22, "rushing_tds": 2, "receiving_yds": 12})
#team2_wr1 = football.Player("Justin Jefferson", "WR", "Minessota Vikings", {"receptions": 4, "receiving_yards": 78, "receiving_tds": 1, "rushing_yards": 0})
#team2_wr2 = football.Player("Deebo Samuel", "WR", "San Fransisco 49ers", {"receptions": 7, "receiving_yards": 113, "receiving_tds": 0, "rushing_yards": 98})
#team2_te1 = football.Player("Sam LaPorta", "TE", "Detroit Lions", {"receptions": 7, "receiving_yds": 84, "receiving_tds": 1})
#team2_defense = football.Player("Ravens Defensive line", "Defense", "Baltimore", {"yards_against": 220, "interceptions": 1, "points_allowed": 14})
#team2_kicker = football.Player("Brandon Aubrey", "Kicker", "Dallas Cowboys", {"FG_made": 1, "PAT_made": 4})
players = football.players_csv("stats 1.csv")
qb1 = players[0]
qb2 = players[1]
team1_rb1 = players[4]
team2_rb1 = players[5]
team1_wr1 = players[8]
team1_wr2 = players[9]
team2_wr1 = players[10]
team2_wr2 = players[11]
team1_te1 = players[16]
team2_te1 = players[17]
team1_defense = players[20]
team2_defense = players[21]
team1_kicker = players[24]
team2_kicker = players[25]


#player1 = players[25]
#print(player1.name)
#print(player1.position)
#print(player1.stats)

team1 = football.Team("Swampdogs", [qb1, team1_wr1, team1_wr2, team1_rb1, team1_te1, team1_defense, team1_kicker])
team2 = football.Team("Golden Stars", [qb2, team2_wr1, team2_wr2, team2_rb1, team2_te1, team2_defense, team2_kicker])

#Foundational level of implementing data and converting to fantasy points
#Next step will be either API or CSV usage
#Once we get a full year season of weekly stats, then we can add in most fantasy football features and simulations
#Another big step is figuring out user interation and giving the user commands
#1

#game = football.Game(team1, team2)
#game.simulate()
