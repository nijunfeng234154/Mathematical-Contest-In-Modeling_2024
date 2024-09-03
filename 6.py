import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('player31.csv')
df.drop('match_id',axis=1,inplace=True)
# Feature engineering (same as before)
# Data preprocessing
X = df.drop('game_victor', axis=1)
y = df['game_victor']

# Split the dataset into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

best_model = RandomForestClassifier(max_depth=36, n_estimators=91, random_state=42)
best_model.fit(X_train_scaled, y_train)

importances = best_model.feature_importances_
feature_names = [col for col in X.columns]
# 将特征名和其重要性值转换为DataFrame
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
})

# 按重要性排序
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
print(feature_importance_df)
from pyecharts.charts import Bar
from pyecharts import options as opts
import numpy as np
# 使用排序后的特征名称和对应的重要性
# 使用排序后的特征名称和对应的重要性
sorted_feature_names = feature_importance_df['Feature'].tolist()
sorted_importances = feature_importance_df['Importance'].tolist()

# 创建条形图
bar = Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))
bar.add_xaxis(sorted_feature_names)
bar.add_yaxis("Feature Importances", sorted_importances, label_opts=opts.LabelOpts(is_show=False))  # 不显示条上的数值
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="Feature Importances"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45, interval=0,font_size=7)),  # 旋转X轴标签以避免重叠
    # datazoom_opts=[opts.DataZoomOpts()],  # 添加数据缩放滑块
    tooltip_opts=opts.TooltipOpts(is_show=True, trigger="axis", axis_pointer_type="cross")  # 显示提示框
)
# 渲染图表到HTML文件，也可以直接使用 render_notebook() 在Jupyter notebook中显示
bar.render('feature_importances.html')