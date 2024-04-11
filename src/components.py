from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(app, df):
    state_options = [{'label': state, 'value': state} for state in df['state_code'].unique()]

    layout = dbc.Container(
        [
            html.H1("U.S. Job Postings Visualization", className="text-center mb-4"),
            html.P(
                """Our dashboard serves as a personalized job market navigator, offering insights into job postings across the US for 2023. It provides job seekers with a clear and interactive overview of the job landscape, enabling them to filter opportunities based on salary range, job type, state codes, and regions.""",
            ),
            # Filters Section
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H5('State Code'),
                            dcc.Dropdown(
                                id='state-dropdown',
                                options=state_options,
                                multi=True,
                                #value=['NY']
                                #value=df['state_code'].unique()
                                value=None
                            ),
                            html.Br(),

                            html.H5("Minimum Salary"),
                            dcc.Slider(
                                id='min-salary-slider',
                                min=0,
                                max=100000,
                                step=1000,
                                value=30000,
                                marks={i: f"${i:,}" for i in range(0, 100001, 20000)},
                                tooltip={"placement": "bottom", "always_visible": True},
                            ),
                            html.Br(),

                            html.H5("Maximum Salary"),
                            dcc.Slider(
                                id='max-salary-slider',
                                min=0,
                                max=100000,
                                step=1000,
                                value=70000,
                                marks={i: f"${i:,}" for i in range(0, 100001, 20000)},
                                tooltip={"placement": "bottom", "always_visible": True},
                            ),
                            html.Br(),

                            html.H5("Job Type"),
                            dbc.Checklist(
                                options=[
                                    {"label": "Full-time", "value": "Full-time"},
                                    {"label": "Part-time", "value": "Part-time"},
                                    {"label": "Contract", "value": "Contract"},
                                ],
                                value=["Full-time"],
                                id='job-type-checklist',
                                inline=True,
                            ),
                            html.Br(),

                            html.H5("Experience Level"),
                            dbc.Checklist(
                                options=[
                                    {"label": "Entry Level", "value": "Entry level"},
                                    {"label": "Mid-Senior Level", "value": "Mid-Senior level"},
                                ],
                                value=["Entry level"],
                                id='experience-level-checklist',
                                inline=True,
                            ),
                        ],
                        md=4,
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id='job-posting'),
                        ],
                        md=8,
                    ),
                ],
                className="mb-4",
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="average-salary-region"), md=4),
                    dbc.Col(dcc.Graph(id="avg-min-max-salary-region"), md=4),
                    dbc.Col(dcc.Graph(id="jobs-by-region-bar-chart"), md=4),
                ]
            ),
            dbc.Row(
                dbc.Col(
                    [
                        html.P(
                            "This dashboard serves as a personalized job market navigator, offering insights based on job postings on Linkedin across the US in 2023. You can select the Job type, Experience level to see the overall salary range in specific regions. The dashboard is made by Andy Zhang, Prabhjit Thind, Sifan Zhang, Yan Zeng.",
                            className="text-center"
                        ),
                        html.P(
                            [
                                "Check the ",
                                html.A("repo", href="https://github.com/UBC-MDS/DSCI-532_2024_21_Job-Postings", target="_blank"),
                                "."
                            ],
                            className="text-center"
                        )
                    ],
                    width={"size": 10, "offset": 1},
                    className="border-top pt-3"
                )
            ),
        ],
        fluid=True,
    )
    return layout
