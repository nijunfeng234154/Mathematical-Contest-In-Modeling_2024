from pyecharts.charts import Bar
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pyecharts.charts import Line
from pyecharts import options as opts
import numpy as np

df = pd.read_csv('train1.csv')
df.drop(['p1_distance_run', 'p1_ace', 'p1_double_fault', 'p1_unf_err','p2_distance_run', 'p2_ace', 'p2_double_fault',
       'p2_unf_err'],axis=1,inplace=True)
df.drop('match_id',axis=1,inplace=True)
df.drop('Unnamed: 0',axis=1,inplace=True)
# 计算相关性
correlation_matrix = df.corr()

# 获取预测变量的相关性并排序
predict_corr = correlation_matrix['turning_point'].sort_values(ascending=False)

# 准备数据
features = predict_corr.index.tolist()
correlations = predict_corr.values.tolist()

# 绘制柱状图
# 绘制横向柱状图
bar = Bar(init_opts=opts.InitOpts(width="800px", height="400px"))
# bar.add_xaxis(features)
# bar.add_yaxis("Correlation with PredictVariable", correlations, label_opts=opts.LabelOpts(is_show=False))
# bar.reversal_axis()  # 使柱子横向展示
# bar.set_global_opts(title_opts=opts.TitleOpts(title="Feature Correlation with PredictVariable", title_textstyle_opts=opts.TextStyleOpts(font_size=10)),
#                     xaxis_opts=opts.AxisOpts(name="Correlation", axislabel_opts=opts.LabelOpts(font_size=8)),
#                     yaxis_opts=opts.AxisOpts(name="Feature", axislabel_opts=opts.LabelOpts(font_size=10)))

# 对于每个柱子，根据相关性数值定义渐变色
for i, correlation in enumerate(correlations):
    color_start = "rgba(255, 255, 255, 0.5)"  # 数值低时的颜色（浅色）
    color_end = "rgba(0, 0, 0, 0.5)"  # 数值高时的颜色（深色）
    # 定义渐变色
    color = opts.ItemStyleOpts(
        color=opts.LinearGradient(
            0, 0, 0, 1,  # 渐变方向
            color_list=[
                (0, color_start),
                (correlation, f"rgba({255 * (1-correlation)}, {0 + 255 * correlation}, {0 + 255 * (1-correlation)}, 0.5)"),  # 渐变中间色
                (1, color_end)
            ]
        )
    )
    # 添加柱子，每个柱子单独设置样式
    bar.add_yaxis("Correlation with PredictVariable", [correlations[i]], label_opts=opts.LabelOpts(is_show=False), itemstyle_opts=color)

bar.reversal_axis()  # 使柱子横向展示
bar.set_global_opts(title_opts=opts.TitleOpts(title="Feature Correlation with PredictVariable", title_textstyle_opts=opts.TextStyleOpts(font_size=10)),
                    xaxis_opts=opts.AxisOpts(name="Correlation", axislabel_opts=opts.LabelOpts(font_size=8)),
                    yaxis_opts=opts.AxisOpts(name="Feature", axislabel_opts=opts.LabelOpts(font_size=10)))


# 显示图表
bar.render('3.html')