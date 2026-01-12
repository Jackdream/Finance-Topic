import pandas as pd

# 从CSV文件读取
inventory = pd.read_csv('../data/shfe_gold_inventory.csv')
print(inventory)
html_table = inventory.to_html(
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
    <h1>产品库存清单</h1>
    {html_table}
</body>
</html>
"""

with open('./output/product_inventory.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
