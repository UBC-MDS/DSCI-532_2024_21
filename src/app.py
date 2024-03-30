from dash import Dash, html, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    html.H1('U.S. Job Postings Visualization', style={'textAlign': 'center'}),
    
    # Filters Section
    html.Div([
        html.Label('Filters'),
        dcc.RangeSlider(
            id='salary-range-slider',
            min=0,
            max=100000,
            step=1000,
            value=[30000, 70000],
            marks={i: '{}'.format(i) if i % 20000 == 0 else '' for i in range(0, 100001, 10000)},
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Label('Job Type'),
        dbc.Checklist(
            options=[
                {"label": "Full-time", "value": "FT"},
                {"label": "Part-time", "value": "PT"},
                {"label": "Contract", "value": "CT"},
            ],
            value=["FT", "PT"],
            id='job-type-checklist',
            inline=True,
        ),
        html.Label('Experience Level'),
        dbc.Checklist(
            options=[
                {"label": "Entry Level", "value": "EL"},
                {"label": "Mid-Senior Level", "value": "MSL"},
            ],
            value=["EL"],
            id='experience-level-checklist',
            inline=True,
        ),
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    # Map and Charts Section
    html.Div([
        dcc.Graph(
            id='job-postings-map',
            figure=go.Figure(),  # Placeholder empty figure
            style={'width': '40%', 'display': 'inline-block'}
        ),
        html.Div([
            dcc.Graph(
                id='average-salary-region',
                figure=go.Figure(),  # Placeholder empty figure
                style={'width': '30%', 'display': 'inline-block'}
            ),
            dcc.Graph(
                id='proportion-job-postings',
                figure=go.Figure(),  # Placeholder empty figure
                style={'width': '30%', 'display': 'inline-block'}
            ),
        ]),
    ], style={'width': '80%', 'display': 'inline-block'}),
    
    # Footer
    html.Div([
        html.P('Data provided by XYZ Corp', style={'textAlign': 'center'}),
    ]),
])

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run_server(debug=True)