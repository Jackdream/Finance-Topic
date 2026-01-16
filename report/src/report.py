import pandas as pd
startDate =  '2026-01-05'
endDate =  '2026-01-09'
# 从CSV文件读取
pd1 = pd.read_csv('../data/黄金价格.csv')
pd1 = pd1[(pd1['日期'] >= startDate) & (pd1['日期'] <= endDate)]

pd2 = pd.read_csv('../data/COMEX黄金库存.csv')
pd2 = pd2[(pd2['日期'] >= startDate) & (pd2['日期'] <= endDate)]
pd2 = pd2.drop(columns=['库存(盎司)','注册黄金(盎司)','合格黄金(盎司)'])

pd3 = pd.read_csv('../data/SPDR黄金ETF库存.csv')
pd3 = pd3[(pd3['日期'] >= startDate) & (pd3['日期'] <= endDate)]
pd3 = pd3.drop(columns=['增持/减持(吨)','总价值(美元)'])

merged_df = pd.merge(pd2, pd3, on='日期', how='outer')
html_table1 = pd1.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

html_table2 = merged_df.to_html(
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
    <title>报告</title>
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
    <h1>黄金整体存量</h1>
    <h1>黄金库存</h1>
    {html_table2}
    <h1>黄金成交量</h1>
    <h1>黄金价格</h1>
    {html_table1}
</body>
</html>
"""

with open('./output/report_2026_01_09.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
