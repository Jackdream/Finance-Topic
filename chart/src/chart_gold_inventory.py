import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取

# COMEX黄金库存
inventory1 = pd.read_csv('../data/comex/COMEX黄金库存.csv', parse_dates=['日期'])
# LBMA黄金库存
inventory2 = pd.read_csv('../data/lbma/LBMA黄金库存(月).csv', parse_dates=['日期'])
# 上期所黄金库存
inventory3 = pd.read_csv('../data/上期所/上期所黄金库存数据(周).csv', parse_dates=['日期'])
# SPDR ETF库存
inventory4 = pd.read_csv('../data/黄金ETF/SPDR黄金ETF库存.csv', parse_dates=['日期'])
# # 中国黄金ETF库存
# inventory5 = pd.read_csv('../data/sge_gold_etf_inventory.csv', parse_dates=['date'])
# # 中国央行黄金库存
# inventory6 = pd.read_csv('../data/pboc_gold.csv', parse_dates=['date'])
# # 全球央行黄金库存
# inventory7 = pd.read_csv('../data/global_central_bank_gold_reserves.csv', parse_dates=['date'])

inventory1 = inventory1.groupby(inventory1['日期'].dt.to_period('M'))['库存(t)'].mean()

intentory1 = inventory1.reset_index()

intentory1['日期'] = intentory1['日期'].dt.to_timestamp()
print(intentory1) 
plt.figure(figsize=(10, 6))

plt.plot(intentory1['日期'], intentory1['库存(t)'], label='库存(吨)', linewidth=0.5)
# plt.plot(inventory2['日期'], inventory2['库存(t)'], label='库存(吨)', linewidth=0.5)
# plt.plot(inventory3['日期'], inventory3['库存(kg)'], label='库存(千克)', linewidth=0.5)
# plt.plot(inventory4['日期'], inventory4['库存(t)'], label='库存(吨)', linewidth=0.5)

plt.axis.major_locator(mdates.MonthLocator())
plt.title('黄金库存', fontsize=16, fontweight='bold', y=1.02)
plt.xlabel('日期', fontsize=12)
plt.ylabel('库存', fontsize=12)

plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()