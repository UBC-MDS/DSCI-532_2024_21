
from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/processed/cleaned_job_postings.csv')

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layout
app.layout = html.Div([
    dbc.Row([
        html.Div('State Code'),
        dcc.Dropdown(
            id='state-dropdown',
            options=[{'label': state, 'value': state} for state in df['state_code'].unique()],
            multi=True,  # Enable multiple selection
            value=['NY']  # Default value
        ),
        html.Br(),
    ]),
    dbc.Row([
        html.Div('Experience Level'),
        dcc.Dropdown(
            id='experience-dropdown',
            options=[{'label': level, 'value': level} for level in df['formatted_experience_level'].dropna().unique()],
            multi=True,  # Enable multiple selection
            value=['Mid-Senior level']  # Default value
        ),
        html.Br(),
    ]),
    # Placeholder for the map
    dcc.Graph(id='job-posting'),
    # Filters Section
    html.Div(
        [
            html.Label("Minimum Salary"),
            dcc.Slider(
                id="min-salary-slider",
                min=0,
                max=100000,
                step=1000,
                value=30000,
                marks={
                    i: "${:,.0f}".format(i) if i % 20000 == 0 else ""
                    for i in range(0, 100001, 10000)
                },
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.Label("Maximum Salary"),
            dcc.Slider(
                id="max-salary-slider",
                min=0,
                max=100000,
                step=1000,
                value=70000,
                marks={
                    i: "${:,.0f}".format(i) if i % 20000 == 0 else ""
                    for i in range(0, 100001, 10000)
                },
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.Label("Job Type"),
            dbc.Checklist(
                options=[
                    {"label": "Full-time", "value": "Full-time"},
                    {"label": "Part-time", "value": "Part-time"},
                    {"label": "Contract", "value": "Contract"},
                ],
                value=["Full-time"],
                id="job-type-checklist",
                inline=True,
            ),
            html.Label("Experience Level"),
            dbc.Checklist(
                options=[
                    {"label": "Entry Level", "value": "Entry level"},
                    {"label": "Mid-Senior Level", "value": "Mid-Senior level"},
                ],
                value=["Entry level"],
                id="experience-level-checklist",
                inline=True,
            ),
        ],
        style={"width": "20%", "display": "inline-block", "verticalAlign": "top"},
    ),
    # Map and Charts Section
    html.Div(
        [
            dcc.Graph(
                id="job-postings-map",
                figure=go.Figure(),  # Placeholder empty figure
                style={"width": "40%", "display": "inline-block"},
            ),
            html.Div(
                [
                    dcc.Graph(
                        id="average-salary-region",
                        style={"width": "30%", "display": "inline-block"},
                    ),
                    dcc.Graph(
                        id="avg-min-max-salary-region",
                        style={"width": "30%", "display": "inline-block"},
                    ),
                    dcc.Graph(
                        id="jobs-by-region-bar-chart",
                        style={"width": "30%", "display": "inline-block"},
                    ),
                ]
            ),
        ],
        style={"width": "80%", "display": "inline-block"},
    ),
    # Footer
    html.Div(
        [
            html.P("Data provided by XYZ Corp", style={"textAlign": "center"}),
        ]
    ),
])


# Define callback for updating the map
@app.callback(
    Output('job-posting', 'figure'),
    [Input('state-dropdown', 'value'), Input('experience-dropdown', 'value')]
)
def update_map(selected_states, selected_experience_levels):
    if not selected_states or not selected_experience_levels:
        return px.choropleth(locations=['USA'], z=[0], color_continuous_scale='Viridis', range_color=(0, 0),
                             title='No Data Selected', mapbox_style="carto-positron")

    df_filtered = df[(df['state_code'].isin(selected_states)) &
                     (df['formatted_experience_level'].isin(selected_experience_levels))]
    median_salary = df_filtered.groupby('state_code')['max_salary'].median().reset_index()

    fig = px.choropleth(median_salary, locations="state_code", color="max_salary",
                        locationmode="USA-states", scope="usa",
                        color_continuous_scale='Viridis',
                        range_color=(median_salary['max_salary'].min(), median_salary['max_salary'].max()),
                        labels={'max_salary': 'Median Max Salary'}, title='Median Max Salary by State')
    fig.update_layout(mapbox_style="carto-positron")

    return fig


# Server side callbacks/reactivity
# Callback for updating the bar chart based on the filters
@app.callback(
    Output("jobs-by-region-bar-chart", "figure"),
    [
        Input("min-salary-slider", "value"),
        Input("max-salary-slider", "value"),
        Input("job-type-checklist", "value"),
        Input("experience-level-checklist", "value"),
    ],
)
def update_bar_chart(
    min_salary, max_salary, selected_job_types, selected_experience_levels
):
    # Start with the full DataFrame
    filtered_df = df.copy()

    # Apply salary filter
    filtered_df = filtered_df[
        (filtered_df["min_salary"] >= min_salary)
        & (filtered_df["max_salary"] <= max_salary)
    ]

    # Apply job type filter
    if selected_job_types:
        filtered_df = filtered_df[
            filtered_df["formatted_work_type"].isin(selected_job_types)
        ]

    # Apply experience level filter
    if selected_experience_levels:
        filtered_df = filtered_df[
            filtered_df["formatted_experience_level"].isin(selected_experience_levels)
        ]

    # Group by region and count the job postings
    jobs_by_region = filtered_df["region"].value_counts().reset_index()
    jobs_by_region.columns = ["region", "count"]

    # Generate the colors for the bar chart dynamically
    region_colors = {
        "West": "blue",
        "Northeast": "green",
        "Southeast": "red",
        "Midwest": "pink",
        "Southwest": "orange",
    }
    bar_colors = [
        region_colors.get(region, "gray") for region in jobs_by_region["region"]
    ]

    # Create a new figure
    figure = go.Figure(
        data=[
            go.Bar(
                x=jobs_by_region["region"],
                y=jobs_by_region["count"],
                marker=dict(color=bar_colors),
            )
        ],
        layout=go.Layout(
            title="Number of Job Postings by Region",
            xaxis=dict(title="Region"),
            yaxis=dict(title="Number of Job Postings"),
            hovermode="closest",
        ),
    )

    return figure


# Run the app/dashboard
if __name__ == '__main__':
    app.run_server(debug=True)


