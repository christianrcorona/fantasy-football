import random
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
                total_points += player.stats.get('receptions', 0)
            elif player.position == "RB":
                total_points += player.stats.get('rushing_yards', 0) / 10 
                total_points += player.stats.get('rushing_tds', 0) * 6  
                total_points += player.stats.get('receptions', 0) * 0.5
            else:
                pass
        return total_points
    


class Game():
    def __init__(self, team1, team2):
        self.team1 = team1 
        self.team2 = team2

    def simulate(self):
        team1_score = self.team1.fantasy_points()
        team2_score = self.team2.fantasy_points()

        print(f'{self.team1.name}: {team1_score}')
        print(f'{self.team2.name}: {team2_score}')

        if team1_score > team2_score:
            winner = self.team1.name
        else:
            winner = self.team2.name

        print(f'Looks like team {winner} won!')

        self.random_occurence(winner, team1_score, team2_score)

    def random_occurence(self, winning_team, team1_score, team2_score):
        while True:
            response = input("Would you like to see a random occurrence? Yes or No: ").lower()
            if response == "no":
                break
            if winning_team == self.team1.name:
                team = self.team1
            else:
                team = self.team2
            player = random.choice(team.roster)
            player.stats['passing_yards'] = player.stats.get('passing_yards', 0) * 0

            print(f"Uh no! {player.name}'s stats have been affected.")

            team.roster.remove(player)
            updated_score = team.fantasy_points()
            team.roster.append(player)

            if team.name == winner:
                if updated_score < team2_score:
                    winner = team2_score.name
                    print(f'What an upset!! {winner} takes the week!')
            else:
                if updated_score > team1_score:
                    winner = team.name
                    print(f'Incredible comeback! {winner} is now taking the week!')
