import plotly.express as px
import pandas as pd


# 从CSV文件读取
message = pd.read_csv('./data/央行购金.csv')
print(message.to_json(orient='records'))