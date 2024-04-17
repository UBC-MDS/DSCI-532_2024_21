from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(app, df):
    state_options = [
        {"label": state, "value": state} for state in df["state_code"].unique()
    ]

    # State Info section with title
    state_info_section = html.Div(
        [
            html.H4("State Info", className="section-title"),
            html.Hr(),

            html.H5("State Code"),
            dcc.Dropdown(
                id="state-dropdown",
                options=state_options,
                multi=True,
                value=None
            ),
        ],
        className='sidebar-section'
    )

    # Region Info section with title, and moved slightly up from the bottom
    region_info_section = html.Div(
        [
            html.H4("Region Info", className="section-title"),
            html.Hr(),

            html.H5("Select Salary Range"),
            dcc.RangeSlider(
                id="salary-range-slider",
                min=0,
                max=100000,
                step=1000,
                value=[30000, 70000],
                marks={i: "${}k".format(i // 1000) if i > 0 else "$0" for i in range(0, 100001, 20000)},
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
                id="job-type-checklist",
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
                id="experience-level-checklist",
                inline=True,
            ),
        ],
        className='sidebar-section',
        style={
            'position': 'absolute',
            'bottom': '10%',
            'left': 0,
            'right': 0,
            'padding': '1rem'
        }
    )

    sidebar = html.Div(
        [
            html.H3("Filters", className="display-4"),
            html.Br(),
            state_info_section,
            html.Div(style={'flex': 1}),
            region_info_section,
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'height': '100vh',
            'padding': '20px',
            'background-color': 'lightblue',
            'position': 'fixed',
            'left': 0,
            'top': 0,
            'width': '20%'
        },
        className='sidebar'
    )


    content = html.Div(
        [
            html.H1("U.S. Job Postings Visualization", className="text-center mb-4"),
            html.Div(id='state-click-info', children="Click on a state in the map to see its region."),

            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="job-posting"), md=12),
                ],
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
                            className="text-center",
                        ),
                        html.P(
                            [
                                "Check the ",
                                html.A(
                                    "repo",
                                    href="https://github.com/UBC-MDS/DSCI-532_2024_21_Job-Postings",
                                    target="_blank",
                                ),
                                ".",
                            ],
                            className="text-center",
                        ),
                    ],
                    width={"size": 10, "offset": 1},
                    className="border-top pt-3",
                )
            ),
        ],
    )

    layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(sidebar, width=3),
                    dbc.Col(content, width=9),
                ],
            ),
        ],
        fluid=True,
    )

    return layout
