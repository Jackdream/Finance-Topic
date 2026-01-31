# 注册金占总库存比例
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取
price = pd.read_csv('../data/COMEX黄金库存.csv')
price = price[(price['日期'] >= '2026-01-26') & (price['日期'] <= '2026-01-30')]
print(price)
df = pd.DataFrame()
df['日期'] = price['日期']
df['比值'] = (price['注册黄金(盎司)'] / price['库存(盎司)']).round(2)

print(df)

# 追加到原数据
existing_df = pd.read_csv('./output/注册金占总库存比例.csv')
print(existing_df)
combined_df = pd.concat([existing_df, df], ignore_index=True)

# 保存
combined_df.to_csv('./output/注册金占总库存比例.csv', index=False)