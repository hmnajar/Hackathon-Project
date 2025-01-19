import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def mapNames(teamName):
    return f"{teamName}Maps.csv"

players = pd.read_csv('players.csv')
playerStats = pd.read_csv('player_data.csv', index_col="Name")


teams = ['100T','2G','C9','EG','FUR','G2','KRU','LEV','LOUD','MIBR','NRG','SEN']

# dictionary
teamPlayers = {teams[i]: players.iloc[:, i].to_list() for i in range(len(teams))}

team1Test = input("Enter a Team: ")
team1mapcsv = mapNames(team1Test)
team2Test = input("Enter opposing Team: ")
team2mapcsv = mapNames(team2Test)
favoredTeam = ""
unfavoredTeam = ""
team1multiplier = 1
team2multiplier = 1
map = input("Enter map: ")


Team1Map = pd.read_csv(team1mapcsv, index_col = 0)
Team2Map = pd.read_csv(team2mapcsv, index_col = 0)

# check winrates
if Team1Map.loc[map, 'win_rate'] == Team2Map.loc[map, 'win_rate']:
    print("No team has a bonus!")
    favoredTeam = team1Test
    unfavoredTeam = team2Test
else:
    if Team1Map.loc[map, 'win_rate'] > Team2Map.loc[map, 'win_rate']:
        print(f"{team1Test} is favored on {map}")
        team1multiplier = 1.33
        favoredTeam = team1Test
        unfavoredTeam = team2Test
        winner_class = 1
    else:
        print(f"{team2Test} is favored on {map}")
        team2multiplier = 1.33
        favoredTeam = team2Test
        unfavoredTeam = team1Test



#  team stats lists
favored_team_statlist = {'ACS': 0, 'K:D': 0, 'KAST': 0, 'CL%': 0, 'FKPR': 0}
unfavored_team_statlist = {'ACS': 0, 'K:D': 0, 'KAST': 0, 'CL%': 0, 'FKPR': 0}

# team with higher map win%
for player in teamPlayers[favoredTeam]:
    if player in playerStats.index:
        player_stats = playerStats.loc[player]
        #print(f"Stats for {player}:")
        favored_team_statlist['ACS'] += player_stats['ACS']
        favored_team_statlist['K:D'] += player_stats['K:D']

        #favored_edited_KAST = int(player_stats['KAST'].rstrip("%"))
        favored_team_statlist['KAST']  += player_stats['KAST']

        #favored_edited_CL = int(player_stats['CL%'].rstrip("%")) 
        favored_team_statlist['CL%'] += player_stats['CL%'] 

        favored_team_statlist['FKPR'] += player_stats['FKPR']
    #else:
        #print(f"Player {player} not found in playerStats.")

for player in teamPlayers[unfavoredTeam]:
    if player in playerStats.index:
        player_stats = playerStats.loc[player]
        #print(f"Stats for {player}:")
        unfavored_team_statlist['ACS'] += player_stats['ACS']
        unfavored_team_statlist['K:D'] += player_stats['K:D']

        #unfavored_edited_KAST = int(player_stats['KAST'].rstrip("%"))
        unfavored_team_statlist['KAST'] += player_stats['KAST']

        #unfavored_edited_CL = int(player_stats['CL%'].rstrip("%"))
        unfavored_team_statlist['CL%'] += player_stats['CL%']

        unfavored_team_statlist['FKPR'] += player_stats['FKPR']
    #else:
        #print(f"Player {player} not found in playerStats.")

weights = { #go back to here
    "ACS": .4,
    "K:D": .4,
    "KAST": .1,
    "CL%": .05,
    "FKPR": .05
}

team1EstScore = sum(favored_team_statlist[stat] * weights[stat] for stat in weights) * team1multiplier
team2EstScore = sum(unfavored_team_statlist[stat] * weights[stat] for stat in weights) * team2multiplier

if (team1EstScore > team2EstScore):
    print(f'{team1Test} is the estimated winner!')
else:
    print(f'{team2Test} is the estimated winner!')

if (team1EstScore > team2EstScore):
    print(f'Estimated odds: {(team2EstScore/team1EstScore) * 100:.2f}%')
else:
    print(f'Estimated odds: {(team1EstScore/team2EstScore) * 100:.2f}%')