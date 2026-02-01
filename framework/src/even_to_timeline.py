import pandas as pd


# 从CSV文件读取
message = pd.read_csv('./data/香港黄金仓库.csv')
message = message.rename(columns={'日期': 'date', '主题':'title', '消息内容':"description", '机构':'tag'})
records = message.to_json(orient='records')
print(message.to_json(orient='records'))

# 格式
# {
#                 id: newId,
#                 date: `2025年${Math.floor(Math.random() * 12) + 1}月`,
#                 title: "新项目",
#                 description: "这是一个新添加的时间线项目描述。",
#                 tag: "新增"
#             };

with open('./resource/timeline.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

html_output = html_template\
        .replace('{{table}}', records)\
        .replace('{{name}}', '香港黄金仓库')
with open('./output/香港黄金仓库.html', 'w', encoding='utf-8') as f:
    f.write(html_output)