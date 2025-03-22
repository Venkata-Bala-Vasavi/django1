import dash
from dash import html, dcc
app = dash.Dash(__name__) 
app.layout = html.Div([ 
    html. H1("23b01a12g0"),
        dcc.Input(placeholder='Enter text here...') 
])
if __name__== '__main__':
    app.run_server(debug=True)