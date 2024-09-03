import pandas

df = pandas.read_csv('test.csv')
df['hold_point_win_p1'] = None
df['hold_point_win_p2'] = None
for index,row in df.iterrows():
    if df['server'][index] == df['point_victor'][index] and df['server'][index] == 1:
        df['hold_point_win_p1'][index] = 1
    if df['server'][index] != df['point_victor'][index] and df['server'][index] == 1:
        df['hold_point_win_p1'][index] = 0
    if df['server'][index] == df['point_victor'][index] and df['server'][index] == 2:
        df['hold_point_win_p2'][index] = 1
    if df['server'][index] != df['point_victor'][index] and df['server'][index] == 2:
        df['hold_point_win_p2'][index] = 0

df.to_csv('test1.csv', index=False)