class Player():
    def __init__(self, name, position, team, stats):
        self.name = name
        self.position = position
        self.team = team
        self.stats = stats

class Team():
    def __init__(self, name, roster):
        self.name = name
        self.roster = roster

    def fantasy_points(self):
        total_points = 0
        for player in self.roster:
            if player.position == "QB":
                total_points += player.stats.get('passing_yards', 0) / 25 
                total_points += player.stats.get('passing_tds', 0) * 6  
                total_points += player.stats.get('rushing_yards', 0) / 10 
                total_points += player.stats.get('rushing_tds', 0) * 6
                total_points -= player.stats.get('interceptions', 0) * 2
            elif player.position == "WR":
                total_points += player.stats.get('receiving_yards', 0) / 10
                total_points += player.stats.get('receiving_tds', 0) * 6
                total_points += player.stats.get('rushing_yards', 0) / 15
            else:
                pass
        return total_points