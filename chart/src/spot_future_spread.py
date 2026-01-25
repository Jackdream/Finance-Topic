# 现货期货价差
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取
price = pd.read_csv('../data/黄金价格.csv')
price = price[(price['日期'] >= '2026-01-19') & (price['日期'] <= '2026-01-23')]
price['价差'] = price['COMEX黄金价格'] - price['LBMA黄金价格']
result = price['价差'].sum() / 5

print(result.round(2))

result = f"2026-01-23,{result.round(2)}\n"
with open('./output/黄金期现价差.csv', 'a', encoding='utf-8') as f:
    f.write(result)