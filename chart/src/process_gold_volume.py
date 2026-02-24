import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件读取
data = pd.read_csv('../data/上期所/上期所黄金交割(月).csv')
data = data[data['期转现(克)'] == 0]
print(data)