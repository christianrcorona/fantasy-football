import random
import pandas as pd

data = pd.read_csv('stats 1.csv')
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
#Based on average scoring systems, multiple resources, in the future, the 0 value in the get method will be useful.
                total_points += player.stats.get('passing_yards', 0) / 25 
                total_points += player.stats.get('passing_tds', 0) * 6  
                total_points += player.stats.get('rushing_yards', 0) / 10 
                total_points += player.stats.get('rushing_tds', 0) * 6
                total_points -= player.stats.get('interceptions', 0) * 2
            elif player.position == "WR":
                total_points += player.stats.get('receiving_yards', 0) / 10
                total_points += player.stats.get('receiving_tds', 0) * 6
                total_points += player.stats.get('rushing_yards', 0) / 15
                total_points += player.stats.get('receptions', 0) * 0.5
            elif player.position == "RB":
                total_points += player.stats.get('rushing_yards', 0) / 10 
                total_points += player.stats.get('rushing_tds', 0) * 6  
                total_points += player.stats.get('total_carries', 0) * 0.3
                total_points += player.stats.get('receiving_yds', 0) / 10
            elif player.position == "TE":
                total_points += player.stats.get('receptions', 0) * 0.5
                total_points += player.stats.get('receiving_yds', 0) / 10
                total_points += player.stats.get('receiving_tds', 0) * 6
            elif player.position == "Defense":
                total_points -= player.stats.get('yards_against', 0) / 35
                total_points += player.stats.get('interceptions', 0) * 2
                total_points -= player.stats.get('points_allowed', 0) / 20
            elif player.position == "Kicker":
                total_points += player.stats.get('FG_made', 0) * 3
                total_points += player.stats.get('PAT_made', 0)
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
        print("")
        print("")
        print("Week 1 of Fantasy Football:")
        print("")
        print("")
        print(f'{self.team1.name}: {team1_score} fantasy points')
        print(f'{self.team2.name}: {team2_score} fantasy points')

        if team1_score > team2_score:
            winner = self.team1.name
        else:
            winner = self.team2.name
        print("")
        print("")
        print(f'Looks like team {winner} won!')
        print("")
        print("")

        new_winner = self.random_occurence(team1_score, team2_score)
        if new_winner:
            # if new_winner returns a value else if it returns none
            winner = new_winner
            print("Updated Winner:", winner)
        else:
            print(f'Looks like it remains the same! {winner} stays on top!')
    def random_occurence(self, team1_score, team2_score):
        response = input("Would you like to see a random occurrence? Yes or No: ").lower()
        print("")
        if response in ['yes', 'y', 'ye', 'yess']:
            teams = [self.team1, self.team2]
            team = random.choice(teams)

            player = random.choice(team.roster)
            
            if player.position == "QB":
                possible_stats = ["passing_yards", "passing_tds", "rushing_yards", "interceptions"]
            elif player.position in ["RB", "WR", "TE"]:
                possible_stats = ["receptions", "receiving_yards", "receiving_tds", "rushing_yards", "total_carries"]
            elif player.position in ["Defense", "Kicker"]:
                possible_stats = ["yards_against", "interceptions", "points_allowed", "FG_made", "PAT_made"]
            else:
                print("New Option")
            
            modify = random.choice(possible_stats)
            original_stat = player.stats.get(modify, 0)
            if original_stat == 0 or original_stat < 0:
                #filtering no data stats
                print(f"{player.name}'s {modify} = 0.\nWe can't perform our magic!")
                print("")
                return None

            operators = ["*", "/"]
            operator = random.choice(operators)

            if operator == "*":
                player.stats[modify] = original_stat * 2
            else:
                player.stats[modify] = original_stat / 30


            print(f"Uh no! {player.name}'s {modify} stat has been affected.\nIt went from: {original_stat} to now {round(player.stats[modify], 2)} .")
            
            updated_score = team.fantasy_points()
            #tests showed that originally was redundant
            print("")
            print(f'The affected team is {team.name}. Here is the updated score\n{round(updated_score, 2)} fantasy points')
            print("")
            if team == self.team1:
                if updated_score < team2_score:
                    #team 1 losing points
                    print(f'What an upset!! {self.team2.name} takes the week!')
                    return self.team2.name
            else:
                if updated_score > team1_score:
                    #team 2 having more points than team 1
                    print(f'Incredible comeback! {team.name} is now taking the week!')
                    return team.name
            player.stats[modify] = original_stat
            #Brings stats back so it can always replay over and over again
        return None
