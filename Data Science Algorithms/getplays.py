import cfbd
import pandas as pd
from cfbd.models.play import Play
from sklearn import linear_model
from sklearn.cluster import HDBSCAN, KMeans
from sklearn import svm

configuration = cfbd.Configuration(
    access_token = 'FdwvuNwhZCikhkr0kboz6oWmIZSf4St1XKC6jMAVgkAGMnFQYsGxDSFBev85ReW4'
)

with cfbd.ApiClient(configuration) as api_client:
    api_instance = cfbd.PlaysApi(api_client)
    plays = api_instance.get_plays(year=2024, season_type ='postseason', team = 'Texas', offense = 'Texas', week = 1)
index = 0
index_list = []
offense_score = []
defense_score = []
period = []
yardline = []
yards_to_goal = []
down = []
distance = []
yards_gained = []
play_type = []
for i in plays:
    index += 1
    index_list.append(index)
    offense_score.append(i.offense_score)
    defense_score.append(i.defense_score)
    period.append(i.period)
    yardline.append(i.yardline)
    yards_to_goal.append(i.yards_to_goal)
    down.append(i.down)
    distance.append(i.distance)
    yards_gained.append(i.yards_gained)
    play_type.append(i.play_type)
plays_df = pd.DataFrame(index_list)
plays_df['offense_score'] = offense_score
plays_df['defense_score'] = defense_score
plays_df['period'] = period
plays_df['yardline'] = yardline
plays_df['yards_to_goal'] = yards_to_goal
plays_df['down'] = down
plays_df['distance'] = distance
plays_df['yards_gained'] = yards_gained
plays_df['play_type'] = play_type
def play_type_converter(x):
    y=0
    if x == 'Pass Incompletion':
        y = 'Pass'
    elif x == 'Pass Reception':
        y = 'Pass'
    elif x == 'Rush':
        y = 'Rush'
    elif x == 'Punt':
        y = 'Punt'
    elif x == 'Pass Touchdown':
        y = 'Pass'
    elif x == 'Field Goal Missed':
        y = 'Kick'
    elif x == 'Rushing Touchdown':
        y = 'Rush'
    elif x == 'Field Goal Good':
        y = 'Kick'
    return y
plays_df['type_conv'] = plays_df['play_type'].apply(play_type_converter)
plays_df_mask = (plays_df['type_conv'] == 'Rush') | (plays_df['type_conv'] == 'Pass')
plays_df = plays_df.loc[plays_df_mask]
plays_df.to_csv('plays.csv')

