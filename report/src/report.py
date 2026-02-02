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

def create_link(url, text=None):
    if pd.isna(url):
        return ''
    if text is None:
        text = url
    return f'<a href="{url}" target="_blank">{text}</a>'

startMonth =  '2025-07'
endMonth =  '2026-01'

lastStartDate =  '2026-01-19'
lastEndDate =  '2026-01-23'
startDate =  '2026-01-26'
endDate =  '2026-01-30'


# 从CSV文件读取
pd1 = pd.read_csv('../data/黄金价格.csv')
pd1 = pd1[(pd1['日期'] >= startDate) & (pd1['日期'] <= endDate)]



html_table1 = pd1.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)


pd4 = pd.read_csv('../data/全球黄金ETF(周).csv')
pd4 = pd4[(pd4['日期'] >= lastStartDate) & (pd4['日期'] <= lastEndDate)]
# pd4 = pd4.drop(columns=['增持/减持(吨)','总价值(美元)'])
pd4 = pd4.rename(columns={'库存(公吨)': '全球黄金ETF(公吨)'})

html_table3 = pd4.to_html(
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


merged_df3 = pd.merge(pd6, pd7, on='日期', how='outer')

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
pd11 = pd11[(pd11['日期'] >= startDate) & (pd11['日期'] <= endDate)]
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
print(pd14)
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

pd18 = pd.read_csv('../data/中国黄金ETF(月).csv')
pd18 = pd18[(pd18['日期'] >= startMonth) & (pd18['日期'] <= endMonth)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table13 = pd18.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd19 = pd.read_csv('../data/LBMA黄金库存(月).csv')
pd19 = pd19[(pd19['日期'] >= startMonth) & (pd19['日期'] <= endMonth)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table14 = pd19.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd20 = pd.read_csv('../data/上海黄金交易所出库量(月).csv')
pd20 = pd20[(pd20['日期'] >= startMonth) & (pd20['日期'] <= endMonth)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table15 = pd20.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd21 = pd.read_csv('../data/上期所黄金库存数据(周).csv')
pd21 = pd21[(pd21['日期'] >= lastStartDate) & (pd21['日期'] <= endDate)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table16 = pd21.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd22 = pd.read_csv('../data/COMEX黄金库存.csv')
pd22 = pd22[(pd22['日期'] >= startDate) & (pd22['日期'] <= endDate)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table17 = pd22.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

pd23 = pd.read_csv('../data/SPDR黄金ETF库存.csv')
pd23 = pd23[(pd23['日期'] >= startDate) & (pd23['日期'] <= endDate)]
# pd13 = pd13.drop(columns=['成交额(人民币)'])
# pd10 = pd10.rename(columns={'黄金储备(t)': '中国央行黄金库存(吨)'})
html_table18 = pd23.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)
# 基础信息
batch_data = [
    ['LBMA黄金交易所', ''],
    ['COMEX黄金期货交易所', ''],
    ['上海黄金期货交易所', ''],
    ['上海黄金交易所', ''],
    ['香港黄金中央清算系统', './香港黄金仓库.html'],
]

infoDf = pd.DataFrame(batch_data, columns=['名称','链接'])
infoDf['显示链接'] = infoDf.apply(lambda row: create_link(row['链接'], row['名称']), axis=1)

html_table21 = infoDf.to_html(
    index=False,
    escape=False,
    classes='product-table',
    border=0,
    justify='left'
)

# 库存量变动
inventoryDf = pd.DataFrame({'日指标': [endDate]})
inventoryDf['COMEX黄金'] = pd22.iloc[-2,1]
inventoryDf['SPDR黄金ETF'] = pd23.iloc[-1,1]
inventoryDf['| 周指标'] = '| ' + endDate
inventoryDf['上期所黄金'] = pd21.iloc[-1,1] / 1000
inventoryDf['全球黄金ETF'] = pd4.iloc[-1,1] * 1.10231
inventoryDf['| 月指标'] = '| ' +pd19.iloc[-1,0]
inventoryDf['LBMA黄金'] = pd19.iloc[-1,1]

inventoryDf['中国央行库存'] = pd7.iloc[-1,1]
inventoryDf['中国黄金ETF'] = pd18.iloc[-1,1]
inventoryDf['| 月指标(全球)'] = '| ' +pd6.iloc[-1,0]
inventoryDf['全球央行库存'] = pd6.iloc[-1,1]

inventorySum =  pd22.iloc[-2,1] + pd23.iloc[-1,1] + pd21.iloc[-1,1] / 1000 + pd4.iloc[-1,1] * 1.10231 + pd19.iloc[-1,1] + pd6.iloc[-1,1]
html_table20 = inventoryDf.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

# 交割量
deliveryDf = pd.DataFrame({'周指标': [pd11.iloc[0,0] + ':' + pd11.iloc[-1,0]]})
deliveryDf['COMEX黄金'] = pd11['交割量(手)'].sum() * 100 * 31.1034768 / 1000 /1000 
deliveryDf['| 周指标(上周)'] = '| ' + pd16.iloc[-1,0]
deliveryDf['上海黄金交易所'] = pd16.iloc[-1,2] / 1000
deliveryDf['| 月指标'] = '| ' +pd14.iloc[-1,0]
deliveryDf['上期所黄金'] = pd14['交割量(克)'].sum() / 1000 / 1000
deliveryDf['| 月指标(上个月)'] = '| ' +pd19.iloc[-2,0]
deliveryDf['上海黄金交易所出库量'] = pd20.iloc[-1,1] / 1000
deliveryDf['LBMA黄金清算量'] = pd19.iloc[-2,2] * 10000 * 31.1034768 / 1000 /1000 
html_table22 = deliveryDf.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

# 变化量表格
df1 = pd.DataFrame({'日指标': [startDate + ':' + endDate]})
df1['黄金价格(美元/盎司)'] = pd1['COMEX黄金价格'].iloc[-1] - pd1['COMEX黄金价格'].iloc[0]
# 库存差值
df1['COMEX黄金(吨)'] = pd22.iloc[-2,1] - pd22.iloc[0,1]
# df1['全球黄金ETF变化(吨)'] = pd4.iloc[-1,1] - pd4.iloc[0,1]

df1['SPDR黄金ETF(吨)'] = pd23.iloc[-1,1] - pd23.iloc[0,1]
# df1['上海黄金交易所黄金(吨)'] = pd21.iloc[-1,1] - pd21.iloc[0,1]
df1['周指标'] = lastStartDate + ":" + endDate
df1['上期所黄金(千克)'] = pd21.iloc[-1,1] - pd21.iloc[0,1]
df1['月指标'] = startMonth + ":" + endMonth
df1['LBMA黄金(吨)'] = pd19.iloc[-1,1] - pd19.iloc[-2,1]
print(df1)
html_table19 = df1.to_html(
    index=False,
    classes='product-table',
    border=0,
    justify='left'
)

with open("../source/新闻/黄金新闻20260130.txt", 'r', encoding='utf-8') as file:
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
            display: block;
            overflow-x: auto;
            white-space: nowrap;
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
    <h2>黄金交易所</h2>
    {html_table21}
    <h2>库存量(吨): {inventorySum}</h2>
    {html_table20}
    <h2>交割量(吨)</h2>
    {html_table22}

    <h2>新闻</h2>
    {content}
</body>
</html>
"""
    # <h1>全球央行</h1>
    # <h2>黄金库存</h2>
    # {html_table4}
    # <h1>全球黄金ETF</h1>
    # <h2>黄金库存</h2>
    # {html_table3}
    # <h1>SPDR黄金ETF</h1>
    # <h2>黄金库存</h2>
    # {html_table18}
    # <h2>黄金租赁</h2>
    # {html_table6}
    # <h1>中国黄金ETF</h1>
    # <h2>黄金库存</h2>
    # {html_table13}
    # <h2>黄金成交量</h2>
    # {html_table12}
    # <h1>LBMA-黄金</h1>
    # <h2>黄金库存</h2>
    # {html_table14}
    # <h2>黄金成交量</h2>
    # {html_table10}
    # <h1>上海黄金交易所-黄金</h1>
    # <h2>黄金库存</h2>
    # {html_table15}
    # <h2>黄金成交量</h2>
    # {html_table11}
    # <h1>上海期货交易所-黄金</h1>
    # <h2>黄金库存</h2>
    # {html_table16}
    # <h2>黄金成交量</h2>
    # {html_table7}
    # <h2>黄金交割量</h2>
    # {html_table8}
    # <h1>COMEX-黄金</h1>
    # <h2>黄金库存</h2>
    # {html_table17}
    # <h2>黄金成交量</h2>
    # {html_table5}
    # <h2>黄金交割量</h2>
    # {html_table9}

with open('./output/report_2026_01_30/index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

