import dash
from dash import html,dcc,Dash, dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


df = pd.read_csv(r'https://www.ncei.noaa.gov/access/monitoring/daily-snow/CO-snowfall-202103.csv')
for col in df.columns:
    print(col)

#print(df[' March 2021'])   
shape = df.shape
print(shape)
app = dash.Dash()
app.layout = dash_table.DataTable(df.to_dict('Colorado Snowfall')) 
app.run_server(debug=True)
