import pandas as pd

# 自定义函数计算连续重复次数
# 计算连续出现次数的函数
def calculate_consecutive_counts(first_value,group):
    # 遍历DataFrame中的每一行
    count1 = 0
    count2 = 0
    prev_value = first_value
    for index,row in group.iterrows():
        if index == group.index[0]:
            group.loc[index, 'count1'] = count1
            group.loc[index, 'count2'] = count2
            continue
        # 如果当前数字与前一个数字相同，增加计数
        if row['point_victor'] == prev_value and prev_value == 1:
            count1 += 1
        elif row['point_victor'] == prev_value and prev_value == 2:
            count2 += 1
        else:
            # 重置计数器
            if  row['point_victor'] != prev_value and prev_value == 1:
                count1 = 0
            elif row['point_victor'] != prev_value and prev_value == 2:
                count2 = 0
        group.loc[index, 'count1'] = count1
        group.loc[index, 'count2'] = count2
        # 更新前一个数字
        prev_value = row['point_victor']

    return group


# 读取数据
df = pd.read_csv('Wimbledon_featured_matches.csv')


# 假设第一列的列名是'Column1'，根据第一列进行分组
grouped_df = df.groupby('match_id')

# 现在，grouped_df包含了一个按照第一列值分组的对象
# 您可以对每个分组执行操作，或者将每个分组保存为一个新的DataFrame

# 例如，遍历每个分组并打印
for name, group in grouped_df:
    print(f'Group name: {name}')
    first_value=group['point_victor'].iloc[0]
    print(calculate_consecutive_counts(first_value,group))


