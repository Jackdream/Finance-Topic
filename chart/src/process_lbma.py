import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件读取
data = pd.read_csv('../data/lbma/LBMA黄金库存(月).csv')
data['库存(t)'] = data['库存(盎司000s)'] * 1000 * 31.1034768 / 1000 /1000 
data['库存(t)'] = data['库存(t)'].round(2)
data.to_csv("./output/LBMA黄金库存.csv", index=False, encoding="utf-8-sig")