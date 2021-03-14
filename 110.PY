import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
data=df['temp'].tolist()
pmean=statistics.mean(data)
pstd=statistics.stdev(data)
print(pmean)
print(pstd)
fig=ff.create_distplot([data],['temp'],show_hist=False)
fig.add_trace(go.Scatter(x=[pmean,pmean],y=[0,1],mode='lines',name='mean'))
fig.show()