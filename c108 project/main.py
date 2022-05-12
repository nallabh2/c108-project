import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

df=pd.read_csv("data.csv")

fig = px.histogram(df, x="Mobile Brand", y="Avg Rating", color="Sr.No", marginal="rug",hover_data=df.columns)
fig.show()
