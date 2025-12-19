import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取
chat_count = pd.read_csv('../data/chat_count_day.csv')
gold_price = pd.read_csv('../data/gold_price.csv')
print(chat_count)
print(gold_price)

merged_df = pd.merge(chat_count, gold_price, on='date', how='outer')
print(merged_df)

fig, ax1 = plt.subplots(figsize=(12, 6))

# 第一个Y轴（左侧）- 温度
color1 = 'tab:red'
ax1.set_xlabel('日期')
ax1.set_ylabel('聊天次数', color=color1, fontsize=12)
line1 = ax1.plot(merged_df['date'], merged_df['count'], color=color1, marker='s', linewidth=2, label='聊天次数')
ax1.tick_params(axis='y', labelcolor=color1)

# 第二个Y轴（右侧）- 销售额
ax2 = ax1.twinx()  # 创建共享x轴的第二个y轴
color2 = 'tab:blue'
ax2.set_ylabel('黄金价格', color=color2, fontsize=12)
line2 = ax2.plot(merged_df['date'], merged_df['price'], color=color2, marker='s', linewidth=2, label='黄金价格')
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('聊天次数与黄金价格对比', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
# ax1.legend(lines1, labels1, loc='upper left')

plt.tight_layout()
plt.show()