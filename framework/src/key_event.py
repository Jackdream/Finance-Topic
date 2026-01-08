import plotly.express as px
import pandas as pd

# 生成示例时间序列数据
date_rng = pd.date_range(start='2025-01-01', end='2025-06-30', freq='D')
df_ts = pd.DataFrame(date_rng, columns=['date'])
df_ts['value'] = np.cumsum(np.random.randn(len(date_rng)))  # 模拟随机游走

# 绘制交互式时间序列
fig = px.line(df_ts, x='date', y='value', title="时间序列趋势图")
fig.update_xaxes(rangeslider_visible=True)  # 添加范围滑动条[5](@ref)
fig.show()