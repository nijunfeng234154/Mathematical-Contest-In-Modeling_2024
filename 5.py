import pandas

df = pandas.read_csv('test.csv')
point_same_values=[]
for index,row in df.iterrows():
    if df['p1_score'][index] == df['p2_score'][index] and df['p1_score'][index] != 0:
        point_same_values.append(1)
    else:
        point_same_values.append(0)

df['same_point'] = point_same_values
df.to_csv('t.csv', index=False)
