import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取
gold_price = pd.read_csv('../data/黄金价格.csv')
print(gold_price)

plt.figure(figsize=(10, 6))

plt.plot(gold_price['日期'], gold_price['COMEX黄金价格'], label='COMEX黄金价格', linewidth=0.5)
plt.plot(gold_price['日期'], gold_price['LBMA黄金价格'], label='LBMA黄金价格', linewidth=0.5)

plt.title('黄金价格', fontsize=16, fontweight='bold', y=1.02)
plt.xlabel('日期', fontsize=12)
plt.ylabel('价格', fontsize=12)

plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()