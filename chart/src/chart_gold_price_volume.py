import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取
gold_price = pd.read_csv('../data/黄金价格.csv')
volume = pd.read_csv('../data/comex/COMEX黄金交易信息.csv')

startDate =  '2025-12-01'
endDate =  '2026-02-27'
gold_price = gold_price[(gold_price['日期'] >= startDate) & (gold_price['日期'] <= endDate)]
volume = volume[(volume['日期'] >= startDate) & (volume['日期'] <= endDate)]

# 2. 创建图表和主坐标轴（左侧Y轴）
fig, ax1 = plt.subplots(figsize=(10, 6))

# 3. 绘制左侧Y轴的折线
line1 = ax1.plot(gold_price['日期'], gold_price['COMEX黄金价格'], color='tab:blue', marker='o', label='黄金价格')
ax1.set_xlabel('日期', fontsize=12)
ax1.set_ylabel('黄金价格', color='tab:blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='tab:blue')  # 设置左侧Y轴刻度文字颜色
ax1.grid(True, alpha=0.3)  # 添加网格，增强可读性

# 4. 创建次坐标轴（右侧Y轴），共享X轴
ax2 = ax1.twinx()

# 5. 绘制右侧Y轴的折线
line2 = ax2.plot(volume['日期'], volume['全部成交量(手)'], color='tab:red', marker='s', label='COMEX成交量')
ax2.set_ylabel('COMEX成交量', color='tab:red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='tab:red')  # 设置右侧Y轴刻度文字颜色
ax2.ticklabel_format(axis='y', style='plain')  

plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)

plt.title('黄金价格与COMEX成交量', fontsize=14, pad=20)
plt.tight_layout()  # 自动调整布局，防止标签重叠
# plt.show()
plt.savefig('./output/COMEX黄金价格与COMXE成交量20260227.png', dpi=300, bbox_inches='tight', facecolor='white')