import pandas as pd
def text_to_html_paragraphs_basic(text):
    """
    基本方法：将文本按空行分割成段落
    
    参数：
    - text: 原始文本
    
    返回：
    - HTML格式的段落
    """
    # 将文本按空行分割（连续换行）
    paragraphs = text.strip().split('\n\n')
    
    # 用<p>标签包裹每个段落
    html_paragraphs = []
    for paragraph in paragraphs:
        if paragraph.strip():  # 只处理非空段落
            # 替换段落内的换行为<br>标签
            formatted_para = paragraph.strip().replace('\n', '<br>')
            html_paragraphs.append(f'<p>{formatted_para}</p>')
    
    return '\n'.join(html_paragraphs)


startMonth =  '2025-07'
endMonth =  '2026-01'

lastStartDate =  '2026-01-05'
lastEndDate =  '2026-01-09'
startDate =  '2026-01-12'
endDate =  '2026-01-16'


# 从CSV文件读取
pd1 = pd.read_csv('../data/黄金价格.csv')
pd1 = pd1[(pd1['日期'] >= startDate) & (pd1['日期'] <= endDate)]

pd2 = pd.read_csv('../data/COMEX黄金库存.csv')
pd2 = pd2[(pd2['日期'] >= startDate) & (pd2['日期'] <= endDate)]
# pd2 = pd2.drop(columns=['库存(盎司)','注册黄金(盎司)','合格黄金(盎司)'])
pd2 = pd2.rename(columns={'库存(t)': 'COMEX黄金库存(吨)'})

pd3 = pd.read_csv('../data/SPDR黄金ETF库存.csv')
pd3 = pd3[(pd3['日期'] >= startDate) & (pd3['日期'] <= endDate)]
# pd3 = pd3.drop(columns=['增持/减持(吨)','总价值(美元)'])
pd3 = pd3.rename(columns={'库存(t)': 'SPDR黄金ETF库存(吨)'})



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

pd4 = pd.read_csv('../data/全球黄金ETF(周).csv')
pd4 = pd4[(pd4['日期'] >= lastStartDate) & (pd4['日期'] <= lastEndDate)]
# pd4 = pd4.drop(columns=['增持/减持(吨)','总价值(美元)'])
pd4 = pd4.rename(columns={'库存(公吨)': '全球黄金ETF(公吨)'})

pd5 = pd.read_csv('../data/上期所黄金库存数据(周).csv')
pd5 = pd5[(pd5['日期'] >= lastStartDate) & (pd5['日期'] <= endDate)]
# pd4 = pd4.drop(columns=['增持/减持(吨)','总价值(美元)'])
pd5 = pd5.rename(columns={'库存(kg)': '上期所黄金库存(kg)'})
merged_df2 = pd.merge(pd4, pd5, on='日期', how='outer')

html_table3 = merged_df2.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd6 = pd.read_csv('../data/全球央行黄金库存.csv')
pd6 = pd6[(pd6['日期'] >= startMonth) & (pd6['日期'] <= endMonth)]
# pd4 = pd4.drop(columns=['增持/减持(吨)','总价值(美元)'])
pd6 = pd6.rename(columns={'库存(t)': '全球央行黄金库存(吨)'})

pd7 = pd.read_csv('../data/中国央行黄金库存.csv')
pd7 = pd7[(pd7['日期'] >= startMonth) & (pd7['日期'] <= endMonth)]
pd7 = pd7.drop(columns=['黄金储备(oz)'])
pd7 = pd7.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})

pd8 = pd.read_csv('../data/中国黄金ETF(月).csv')
pd8 = pd8[(pd8['日期'] >= startMonth) & (pd8['日期'] <= endMonth)]
# pd8 = pd8.drop(columns=['黄金储备(oz)'])
pd8 = pd8.rename(columns={'库存(t)': '中国黄金ETF(吨)'})

pd9 = pd.read_csv('../data/LBMA黄金库存(月).csv')
pd9 = pd9[(pd9['日期'] >= startMonth) & (pd9['日期'] <= endMonth)]
pd9 = pd9.drop(columns=['清算数据(万盎司)'])
pd9 = pd9.rename(columns={'库存(t)': 'LBMA黄金库存(吨)'})

merged_df3 = pd.merge(pd6, pd7, on='日期', how='outer')
merged_df3 = pd.merge(merged_df3, pd8, on='日期', how='outer')
merged_df3 = pd.merge(merged_df3, pd9, on='日期', how='outer')

html_table4 = merged_df3.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd10 = pd.read_csv('../data/COMEX黄金交易信息.csv')
pd10 = pd10[(pd10['日期'] >= lastStartDate) & (pd10['日期'] <= endDate)]
# pd10 = pd10.drop(columns=['成交量'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})

pd11 = pd.read_csv('../data/COMEX黄金交割.csv')
pd11 = pd11[(pd11['日期'] >= lastStartDate) & (pd11['日期'] <= endDate)]
# pd11 = pd11.drop(columns=['成交量'])
# pd11 = pd11.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})

# merged_df4 = pd.merge(pd10, pd11, on='日期', how='outer')
html_table5 = pd10.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

html_table9 = pd11.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd12 = pd.read_csv('../data/SPDR黄金ETF租赁.csv')
pd12 = pd12[(pd12['日期'] >= startDate) & (pd12['日期'] <= endDate)]
# pd12 = pd12.drop(columns=['成交量'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table6 = pd12.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd13 = pd.read_csv('../data/上期所交易数据.csv')
pd13 = pd13[(pd13['日期'] >= startDate) & (pd13['日期'] <= endDate)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table7 = pd13.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd14 = pd.read_csv('../data/上期所黄金交割(月).csv')
pd14 = pd14[(pd14['日期'] >= startMonth) & (pd14['日期'] <= endMonth)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table8 = pd14.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd15 = pd.read_csv('../data/LBMA黄金成交量.csv')
# pd15 = pd15[(pd15['日期'] >= startMonth) & (pd15['日期'] <= endMonth)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table10 = pd15.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd16 = pd.read_csv('../data/上海黄金交易所交易数据.csv')
pd16 = pd16[(pd16['日期'] >= lastStartDate) & (pd16['日期'] <= endDate)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table11 = pd16.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd17 = pd.read_csv('../data/中国黄金成交量.csv')
pd17 = pd17[(pd17['日期'] >= startDate) & (pd17['日期'] <= endDate)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table12 = pd17.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

with open("../source/新闻/黄金新闻20260116.txt", 'r', encoding='utf-8') as file:
    content = file.read()

content = text_to_html_paragraphs_basic(content)
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

        h2,p {{
            text-align: left;
            color: #2c3e50;
            width: 90%;
            border-collapse: collapse;
            margin: 20px auto;
        }}
    </style>
</head>
<body>
    <h1>黄金报告</h1>
    <h2>黄金价格</h1>
    {html_table1}
    <h2>黄金库存(月)</h2>
    {html_table4}
    <h2>黄金库存(周)</h2>
    {html_table3}
    <h2>黄金库存(日)</h2>
    {html_table2}
    <h1>中国黄金ETF</h1>
    <h2>黄金成交量</h2>
    {html_table12}
    <h1>LBMA-黄金</h1>
    <h2>黄金成交量</h2>
    {html_table10}
    <h1>上海黄金交易所-黄金</h1>
    <h2>黄金成交量</h2>
    {html_table11}
    <h1>上海期货交易所-黄金</h1>
    <h2>黄金成交量</h2>
    {html_table7}
    <h2>黄金交割量</h2>
    {html_table8}
    <h1>COMEX-黄金</h1>
    <h2>黄金成交量</h2>
    {html_table5}
    <h2>黄金交割量</h2>
    {html_table9}
    <h2>黄金租赁</h2>
    {html_table6}
    <h2>新闻</h2>
    {content}
</body>
</html>
"""

with open('./output/report_2026_01_16.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

