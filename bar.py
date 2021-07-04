import pandas as pd

import plotly.express as px

fig = px.bar(x='date', y='cases',color='country', title='Corona cases')
fig.show()