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
# 中国央行黄金库存
inventory6 = pd.read_csv('../data/pboc_gold.csv', parse_dates=['date'])
# 全球央行黄金库存
inventory7 = pd.read_csv('../data/global_central_bank_gold_reserves.csv', parse_dates=['date'])

print(['date'])
# 拿最新数据
inventoryLine1 = inventory1.loc[inventory1.index.max()]
name1 = "COMEX库存(t)("  + inventoryLine1['date'].strftime("%Y-%m-%d") + ")"
inventory1 = inventoryLine1.to_frame().T
inventory1['date'] = pd.to_datetime(inventory1['date'])
inventory1 = inventory1.reset_index(drop=True)
inventory1 = inventory1.rename(columns={'inventory(t)': name1})

inventoryLine2 = inventory2.loc[inventory2.index.max()]
name2 = "LBMA库存(t)("  + inventoryLine2['date'].strftime("%Y-%m-%d") + ")"
inventory2 = inventoryLine2.to_frame().T
inventory2['date'] = pd.to_datetime(inventory2['date'])
inventory2 = inventory2.reset_index(drop=True)
inventory2 = inventory2.rename(columns={'inventory(t)': name2})

inventoryLine3 = inventory3.loc[inventory3.index.max()]
name3 = "上期所库存(kg)("  + inventoryLine3['date'].strftime("%Y-%m-%d") + ")"
inventory3 = inventoryLine3.to_frame().T
inventory3['date'] = pd.to_datetime(inventory3['date'])
inventory3 = inventory3.reset_index(drop=True)
inventory3 = inventory3.rename(columns={ 'inventory(kg)': name3})

inventoryLine4 = inventory4.loc[inventory4.index.max()]
name4 = "SPDR-ETF库存(t)("  + inventoryLine4['date'].strftime("%Y-%m-%d") + ")"
inventory4 = inventoryLine4.to_frame().T
inventory4['date'] = pd.to_datetime(inventory4['date'])
inventory4 = inventory4.reset_index(drop=True)
inventory4 = inventory4.rename(columns={ '库存(t)': name4})

inventoryLine5 = inventory5.loc[inventory5.index.max()]
name5 = "中国黄金ETF库存(t)("  + inventoryLine5['date'].strftime("%Y-%m-%d") + ")"
inventory5 = inventoryLine5.to_frame().T
inventory5['date'] = pd.to_datetime(inventory5['date'])
inventory5 = inventory5.reset_index(drop=True)
inventory5 = inventory5.rename(columns={'inventory(t)': name5})

inventoryLine6 = inventory6.loc[inventory6.index.max()]
name6 = "中国央行黄金库存(t)("  + inventoryLine6['date'].strftime("%Y-%m-%d") + ")"
inventory6 = inventoryLine6.to_frame().T
inventory6['date'] = pd.to_datetime(inventory6['date'])
inventory6 = inventory6.reset_index(drop=True)
inventory6 = inventory6.rename(columns={'黄金储备(t)': name6})

inventoryLine7 = inventory7.loc[inventory6.index.max()]
name6 = "中国央行黄金库存(t)("  + inventoryLine7['date'].strftime("%Y-%m-%d") + ")"
inventory6 = inventoryLine6.to_frame().T
inventory6['date'] = pd.to_datetime(inventory6['date'])
inventory6 = inventory6.reset_index(drop=True)
inventory6 = inventory6.rename(columns={'黄金储备(t)': name6})

# 库存相加

merged_df = pd.concat([inventory1, inventory2, inventory4, inventory3, inventory5, inventory6], axis=1)
# merged_df = pd.merge(inventory1, inventory2, on='date', how='outer')
# merged_df = pd.merge(merged_df, inventory3, on='date', how='outer')
# merged_df = pd.merge(merged_df, inventory4, on='date', how='outer')
# merged_df = pd.merge(merged_df, inventory5, on='date', how='outer')
# merged_df = merged_df.rename(columns={'inventory(t)_x': 'COMEX库存(t)','inventory(kg)': '上期所库存(kg)', 
# 'inventory(t)_y': 'LBMA库存(t)', '库存(t)': 'SPDR-ETF库存(t)', 'inventory(t)': '中国黄金ETF(t)'})
merged_df = merged_df.drop(columns=['inventory(oz)', 'date', '黄金储备(oz)'])
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