import random
import pandas as pd

def players_csv(file):
    data = pd.read_csv(file)
    players = data.apply(Player, axis=1).tolist()
    return players

class Player():
    def __init__(self, row):
        self.name = row["Player Name"]
        self.position = row["Position"]
        self.stats = {key: value for key, value in {
            "Passing Yards": float(row["Passing Yards"]) if not pd.isna(row["Passing Yards"]) else None,
            "Passing Touchdowns": float(row["Passing Touchdowns"]) if not pd.isna(row["Passing Touchdowns"]) else None,
            "Rushing Yards": float(row["Rushing Yards"]) if not pd.isna(row["Rushing Yards"]) else None,
            "Rushing Touchdowns": float(row["Rushing Touchdowns"]) if not pd.isna(row["Rushing Touchdowns"]) else None,
            "Interceptions": float(row["Interceptions"]) if not pd.isna(row["Interceptions"]) else None,
            "RB Total Rushing Yards": float(row["RB Total Rushing Yards"]) if not pd.isna(row["RB Total Rushing Yards"]) else None,
            "RB Total Rushing Carries": float(row["RB Total Rushing Carries"]) if not pd.isna(row["RB Total Rushing Carries"]) else None,
            "RB Total Rushing Touchdowns": float(row["RB Total Rushing Touchdowns"]) if not pd.isna(row["RB Total Rushing Touchdowns"]) else None,
            "RB Receiving Yards": float(row["RB Receiving Yards"]) if not pd.isna(row["RB Receiving Yards"]) else None,
            "WR Total Receptions": float(row["WR Total Receptions"]) if not pd.isna(row["WR Total Receptions"]) else None,
            "WR Total Receiving Yards": float(row["WR Total Receiving Yards"]) if not pd.isna(row["WR Total Receiving Yards"]) else None,
            "WR Total Receiving Touchdowns": float(row["WR Total Receiving Touchdowns"]) if not pd.isna(row["WR Total Receiving Touchdowns"]) else None,
            "WR Rushing Yards": float(row["WR Rushing Yards"]) if not pd.isna(row["WR Rushing Yards"]) else None,
            "TE Total Receptions": float(row["TE Total Receptions"]) if not pd.isna(row["TE Total Receptions"]) else None,
            "TE Total Yards": float(row["TE Total Yards"]) if not pd.isna(row["TE Total Yards"]) else None,
            "TE Receiving Touchdowns": float(row["TE Receiving Touchdowns"]) if not pd.isna(row["TE Receiving Touchdowns"]) else None,
            "Total Yards Against": float(row["Total Yards Against"]) if not pd.isna(row["Total Yards Against"]) else None,
            "Total Interceptions": float(row["Total Interceptions"]) if not pd.isna(row["Total Interceptions"]) else None,
            "Total Points Allowed": float(row["Total Points Allowed"]) if not pd.isna(row["Total Points Allowed"]) else None,
            "Total FG Made": float(row["Total FG Made"]) if not pd.isna(row["Total FG Made"]) else None,
            "Total PAT Made": float(row["Total PAT Made"]) if not pd.isna(row["Total PAT Made"]) else None
    }.items() if value is not None}
        
class Team():
    def __init__(self, name, roster):
        self.name = name
        self.roster = roster

    def fantasy_points(self):
        total_points = 0
        for player in self.roster:
            if player.position == "QB":
#Based on average scoring systems, multiple resources, in the future, the 0 value in the get method will be useful.
                total_points += player.stats.get('Passing Yards', 0) / 25 
                total_points += player.stats.get('Passing Touchdowns', 0) * 6  
                total_points += player.stats.get('Rushing Yards', 0) / 10 
                total_points += player.stats.get('Rushing Touchdowns', 0) * 6
                total_points -= player.stats.get('Interceptions', 0) * 2
            elif player.position == "WR":
                total_points += player.stats.get('WR Total Receiving Yards', 0) / 10
                total_points += player.stats.get('WR Total Receiving Touchdowns', 0) * 6
                total_points += player.stats.get('WR Rushing Yards', 0) / 15
                total_points += player.stats.get('WR Total Receptions', 0) * 0.5
            elif player.position == "RB":
                total_points += player.stats.get('RB Total Rushing Yards', 0) / 10 
                total_points += player.stats.get('RB Total Rushing Touchdowns', 0) * 6  
                total_points += player.stats.get('RB Total Rushing Carries', 0) * 0.3
                total_points += player.stats.get('RB Receiving Yards', 0) / 10
            elif player.position == "TE":
                total_points += player.stats.get('TE Total Receptions', 0) * 0.5
                total_points += player.stats.get('TE Total Yards', 0) / 10
                total_points += player.stats.get('TE Receiving Touchdowns', 0) * 6
            elif player.position == "Defense":
                total_points -= player.stats.get('Total Yards Against', 0) / 35
                total_points += player.stats.get('Total Interceptions', 0) * 2
                total_points -= player.stats.get('Total Points Allowed', 0) / 20
            elif player.position == "Kicker":
                total_points += player.stats.get('Total FG Made', 0) * 3
                total_points += player.stats.get('Total PAT Made', 0)
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
