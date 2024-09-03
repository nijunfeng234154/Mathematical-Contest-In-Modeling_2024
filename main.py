import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.globals import ThemeType

df1 = pd.read_csv('player1_test.csv')
df2 = pd.read_csv('player2_test.csv')

match_id = "2023-wimbledon-1701"
df1 = df1[df1['match_id'] == match_id]
df2 = df2[df2['match_id'] == match_id]

#数据标准化处理
df1.drop('match_id',axis=1,inplace=True)
df2.drop('match_id',axis=1,inplace=True)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
df1_scaled = scaler.fit_transform(df1)
df2_scaled = scaler.fit_transform(df2)

y1=None
# 初始化一个列表来保存计算的y1值
y1_values = []
sum1=0
# 使用 iterrows() 正确迭代 DataFrame
for index, row in df1.iterrows():
    y1 = (0.11 * row['break_point_win_p1'] +
          0.036 * row['be_break_point_win_p1'] +
          0.55 * row['hold_point_win_p1'] +
          0.099 * row['consecutive_points_p1'] +
          0.011 * row['p1_distance_run'])
    sum1+=y1
    y1_values.append(sum1)
df1['y1'] = y1_values

y2=None
# 绘制折线图
plt.figure(figsize=(10, 6))
# 初始化一个列表来保存计算的y1值
y2_values = []
sum2=0
# 使用 iterrows() 正确迭代 DataFrame
for index, row in df2.iterrows():
    y2 = (0.55 * row['break_point_win_p2'] +
          0.44 * row['be_break_point_win_p2'] +
          0.190 * row['hold_point_win_p2'] +
          0.024 * row['consecutive_points_p2'] +
          0.008 * row['p2_distance_run'])
    sum2+=y2
    y2_values.append(sum2)
df2['y2'] = y2_values

from pyecharts.charts import Line
from pyecharts import options as opts

# 创建折线图对象
line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1400px", height="700px"))

# 添加X轴数据
line.add_xaxis(df1.index.tolist())

# 添加Y轴数据
line.add_yaxis("Carlos Alcaraz", df1['y1'].tolist(), is_smooth=True, label_opts=opts.LabelOpts(is_show=True), color="blue")
line.add_yaxis("Novak Djokovic", df2['y2'].tolist(), is_smooth=True, label_opts=opts.LabelOpts(is_show=True), color="red")

# 设置全局配置
line.set_global_opts(title_opts=opts.TitleOpts(title="Complex Momentum Score Throughout the Match"),
                     xaxis_opts=opts.AxisOpts(name="Point Number"),
                     yaxis_opts=opts.AxisOpts(name="Momentum Score"),
                     legend_opts=opts.LegendOpts(is_show=True))

# 保存图表为HTML文件
line.render('momentum_score_match.html')
