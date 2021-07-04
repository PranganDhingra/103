import pandas as pd
import plotly.express as px

fig = px.scatter(x="date", y="cases",color="country",title='Corona Cases')
fig.show()