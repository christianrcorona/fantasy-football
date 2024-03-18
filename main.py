import football

qb1 = football.Player("Mac Jones", "QB", "Jacksonville Jaguars", {"passing_yards": 316, "passing_tds": 3, "rushing_yards": 15, "rushing_tds": 0, "interceptions": 1})
qb2 = football.Player("Tua Tagovailoa", "QB", "Miami Dolphins", {"passing_yards": 466, "passing_tds": 3, "rushing_yards": 5, "rushing_tds": 0, "interceptions": 1})
wr1 = football.Player("Tyreek Hill", "WR", "Miami Dolphins", {"receiving_yards": 215, "receiving_tds": 2, "rushing_yards": 0})
wr2 = football.Player("Stefon Diggs", "WR", "Buffalo Bills", {"receiving_yards": 102, "receiving_tds": 1, "rushing_yards": 0})
team1 = football.Team("Swampdogs", [qb1, wr1])
team2 = football.Team("Golden Stars", [qb2, wr2])
score1 = team1.fantasy_points()
score2 = team2.fantasy_points()
print(f'Team 1 has a score of: {score1}')
print(f'Team 2 has a score of: {score2}')
