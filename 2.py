import pandas as pd

df = pd.read_csv('player2.csv')

for index,row in df.iterrows():
    i = index
    j = i
    while df['game_victor'][i] == 0:
        j+=1
        if df['game_victor'][j] == 1 or df['game_victor'][j] == 2:
            break
    if df['game_victor'][j] == 1:
        df['game_victor'][i:j] = 0
    else:
        df['game_victor'][i:j] = 1

df.to_csv('player2_test.csv',index=False)
