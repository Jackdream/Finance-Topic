import pandas as pd
import json
print("当前pandas版本：", pd.__version__)

def create_link(url, text=None):
    if pd.isna(url):
        return ''
    if text is None:
        text = url
    return f'<a href="{url}" target="_blank">{text}</a>'
def get_arr(data):
    return [data]

# 从CSV文件读取
message = pd.read_csv('./data/中国黄金协会.csv')
message['details'] = message['消息内容'].apply(get_arr)
# message['summary'] = message.apply(lambda row: create_link(row['链接'], '跳转'), axis=1)
# message['summary'] =''
message = message.rename(columns={'日期': 'date', '主题':'title', '机构':'author','链接':'summary'})

json_str = message.to_json(orient='records')
# records = message.to_dict(orient='records')
# json_str = json.dumps(records, ensure_ascii=False, indent=4)

# 格式
#   {
#         id: 1,
#         title: "日央行加息",
#         date: "2025-12-22",
#         author: "无",
#         summary: "日央行加息",
#         details: [
#             "有两件事值得注意：一是美联储提前开启了QE，并准备了巨额的风险准备资金。显然，美头部已经开始准备即将开始的深刻调整。二是日本加息并未触动逆向套息交易。甚至，日元汇率出现了令人愕然的贬值。",
#             "美联储的放水动作，证明美资本市场已经出现美元短缺。原因，在于流速。至于日元汇率，应是日央行抛售美债的动作被强行管控了。美国的做法，令人耳目一新，在三角悖论中，美国选择了管控自由兑换。",
#         ]
#     },

with open('./resource/list.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

html_output = html_template\
        .replace('{{table}}', json_str)\
        .replace('{{title}}', '中国黄金协会')
with open('./output/中国黄金协会.html', 'w', encoding='utf-8') as f:
    f.write(html_output)