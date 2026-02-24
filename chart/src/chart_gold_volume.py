import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 成交量

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取
gold_price = pd.read_csv('../data/上期所/上期所交易数据.csv')
print(gold_price)

plt.figure(figsize=(10, 6))
plt.ticklabel_format(axis='y', style='plain')  
plt.plot(gold_price['日期'], gold_price['成交量(手)'], label='成交量(手)', linewidth=0.5)

plt.title('成交量', fontsize=16, fontweight='bold', y=1.02)
plt.xlabel('日期', fontsize=12)
plt.ylabel('手', fontsize=12)

plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()