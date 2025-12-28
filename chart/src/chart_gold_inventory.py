import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从CSV文件读取

# COMEX黄金库存
inventory1 = pd.read_csv('../data/comex_gold_inventory.csv', parse_dates=['date'])
# LBMA黄金库存
inventory2 = pd.read_csv('../data/lbma_gold_inventory.csv', parse_dates=['date'])
# 上期所黄金库存
inventory3 = pd.read_csv('../data/shfe_gold_inventory.csv', parse_dates=['date'])
# SPDR ETF库存
inventory4 = pd.read_csv('../data/spdr_gold_inventory.csv', parse_dates=['date'])
# 中国黄金ETF库存
inventory5 = pd.read_csv('../data/sge_gold_etf_inventory.csv', parse_dates=['date'])

inventory1 = inventory1.loc[inventory1.index.max()].to_frame().T
inventory1['date'] = pd.to_datetime(inventory1['date'])
inventory1 = inventory1.reset_index(drop=True)
inventory1 = inventory1.rename(columns={'inventory(t)': 'COMEX库存(t)'})

inventory2 = inventory2.loc[inventory2.index.max()].to_frame().T
inventory2['date'] = pd.to_datetime(inventory2['date'])
inventory2 = inventory2.reset_index(drop=True)
inventory2 = inventory2.rename(columns={'inventory(t)': 'LBMA库存(t)'})

inventory3 = inventory3.loc[inventory3.index.max()].to_frame().T
inventory3['date'] = pd.to_datetime(inventory3['date'])
inventory3 = inventory3.reset_index(drop=True)
inventory3 = inventory3.rename(columns={ 'inventory(kg)': '上期所库存(kg)'})

inventory4 = inventory4.loc[inventory4.index.max()].to_frame().T
inventory4['date'] = pd.to_datetime(inventory4['date'])
inventory4 = inventory4.reset_index(drop=True)
inventory4 = inventory4.rename(columns={ '库存(t)': 'SPDR-ETF库存(t)'})

inventory5 = inventory5.loc[inventory5.index.max()].to_frame().T
inventory5['date'] = pd.to_datetime(inventory5['date'])
inventory5 = inventory5.reset_index(drop=True)
inventory5 = inventory5.rename(columns={'inventory(t)': '中国黄金ETF(t)'})

merged_df = pd.concat([inventory1, inventory2, inventory3, inventory4, inventory5], axis=1)
# merged_df = pd.merge(inventory1, inventory2, on='date', how='outer')
# merged_df = pd.merge(merged_df, inventory3, on='date', how='outer')
# merged_df = pd.merge(merged_df, inventory4, on='date', how='outer')
# merged_df = pd.merge(merged_df, inventory5, on='date', how='outer')
# merged_df = merged_df.rename(columns={'inventory(t)_x': 'COMEX库存(t)','inventory(kg)': '上期所库存(kg)', 
# 'inventory(t)_y': 'LBMA库存(t)', '库存(t)': 'SPDR-ETF库存(t)', 'inventory(t)': '中国黄金ETF(t)'})
merged_df = merged_df.drop(columns=['inventory(oz)'])
print(merged_df)
html_table = merged_df.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>产品库存表</title>
    <style>
        .product-table {{
            width: 90%;
            border-collapse: collapse;
            margin: 20px auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .product-table th {{
            background-color: #2c3e50;
            color: white;
            padding: 15px;
            text-align: left;
        }}
        .product-table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #dddddd;
        }}
        .product-table tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        .product-table tr:hover {{
            background-color: #e9f7fe;
        }}
        h1 {{
            text-align: center;
            color: #2c3e50;
        }}
    </style>
</head>
<body>
    <h1>产品库存清单</h1>
    {html_table}
</body>
</html>
"""

with open('./output/product_inventory.html', 'w', encoding='utf-8') as f:
    f.write(full_html)