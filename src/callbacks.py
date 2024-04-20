from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
from flask_caching import Cache
import dash


def register_callbacks(
    app,
    df,
    jobs_by_region,
    avg_min_max_salaries_by_region,
    region_colors,
):

    # Setup cache
    cache = Cache(
        app.server,
        config={
            "CACHE_TYPE": "filesystem",
            "CACHE_DIR": "cache-directory",
            "CACHE_DEFAULT_TIMEOUT": 300,  # Cache timeout in seconds
        },
    )

    # edited by Andy Z.
    @app.callback(Output("job-posting", "figure"), [Input("state-dropdown", "value")])
    @cache.memoize(timeout=300)  # Cache for 5 minutes
    def update_graph(selected_states=None):
        """
        Update the map based on the selected states.

        This callback function filters the job postings data frame based on the selected states
        and updates the map to display the median of the maximum salary for each state.
        If no states are selected, the map displays data for all states.

        Parameters
        ----------
        selected_states : list of str, optional
            The list of selected state codes. If None, all states are considered.

        Returns
        -------
        dict
            A Plotly figure object represented as a dictionary, which is used to update the
            map in the Dash application.
        """
        subdf = df[df["pay_period"] == "YEARLY"]
        df_filtered = subdf
        if selected_states:
            df_filtered = subdf[subdf["state_code"].isin(selected_states)]

        median_salary = (
            df_filtered.groupby("state_code")["max_salary"].median().reset_index()
        )
        median_salary_1 = (
            subdf.groupby("state_code")["max_salary"].median().reset_index()
        )

        fig = px.choropleth(
            median_salary,
            locations="state_code",
            color="max_salary",
            locationmode="USA-states",
            scope="usa",
            color_continuous_scale="deep",
            range_color=(
                median_salary_1["max_salary"].min(),
                median_salary_1["max_salary"].max(),
            ),
            labels={"max_salary": "Median of `The Max Salary`"},
        )

        fig.update_layout(
            mapbox_style="carto-positron",
            title_x=0.5,
            height=700,
            width=1200,
        )

        fig.update_traces(
            colorbar=dict(
                title="Median of `The Max Salary`",
                tickvals=[
                    median_salary["max_salary"].min(),
                    median_salary["max_salary"].max(),
                ],
                ticktext=[
                    median_salary["max_salary"].min(),
                    median_salary["max_salary"].max(),
                ],
            )
        )

        return fig



    @app.callback(
        Output('state-dropdown', 'value'),
        [
            Input('job-posting', 'clickData'),
            Input('job-posting', 'selectedData'),
            State('state-dropdown', 'value')
        ]
    )
    @cache.memoize(timeout=300)  # Cache for 5 minutes
    def update_dropdown_value(click_data, selected_data, current_value):
        """
        Update the values of the state dropdown based on user interactions with the choropleth map.

        This callback updates the dropdown values when a state is clicked or when multiple states
        are selected using the lasso tool on the map. Clicking an already selected state removes it
        from the selections.

        Parameters
        ----------
        click_data : dict
            Data corresponding to the click event on the map. Contains the clicked state code.
        selected_data : dict
            Data corresponding to the lasso selection on the map. Contains state codes of all selected states.
        current_value : list of str
            The current list of state codes selected in the dropdown.

        Returns
        -------
        list of str
            The updated list of state codes for the dropdown, reflecting the latest user interactions with the map.
        """
        ctx = dash.callback_context
        
        if not ctx.triggered:
            input_id = 'No input yet'
        else:
            input_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if input_id == 'job-posting' and click_data:
            # Handle click data
            clicked_state = click_data['points'][0]['location']
            
            if current_value is None:
                return [clicked_state]
            elif clicked_state in current_value:
                current_value.remove(clicked_state)
            else:
                current_value.append(clicked_state)
                
        elif input_id == 'job-posting' and selected_data:
            # Handle lasso select tool data
            selected_states = [point['location'] for point in selected_data['points']]
            current_value = list(set(current_value + selected_states if current_value else selected_states))
            
        return current_value



    @app.callback(
        Output("jobs-by-region-bar-chart", "figure"),
        [
            Input("salary-range-slider", "value"),
            Input("job-type-checklist", "value"),
            Input("experience-level-checklist", "value"),
        ],
    )
    @cache.memoize(timeout=300)  # Cache for 5 minutes
    def update_bar_chart(salary_range, selected_job_types, selected_experience_levels):
        """
        Update the bar chart to display the number of job postings by region.

        Filters the dataset based on user-selected salary range, job types, and experience levels,
        then counts the number of job postings per region and displays this information in a bar chart.

        Parameters
        ----------
        salary_range : list of [int, int]
            A two-element list specifying the minimum and maximum salary range for filtering job postings.
        selected_job_types : list of str
            A list of job types selected by the user for filtering.
        selected_experience_levels : list of str
            A list of experience levels selected by the user for filtering.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object containing the updated bar chart of job postings by region.
        """
        min_salary, max_salary = salary_range
        filtered_df = df.copy()
        filtered_df = filtered_df[
            (filtered_df["min_salary"] >= min_salary)
            & (filtered_df["max_salary"] <= max_salary)
        ]
        if selected_job_types:
            filtered_df = filtered_df[
                filtered_df["formatted_work_type"].isin(selected_job_types)
            ]
        if selected_experience_levels:
            filtered_df = filtered_df[
                filtered_df["formatted_experience_level"].isin(
                    selected_experience_levels
                )
            ]

        jobs_by_region_filtered = filtered_df["region"].value_counts().reset_index()
        jobs_by_region_filtered.columns = ["region", "count"]
        bar_colors = [
            region_colors.get(region, "gray")
            for region in jobs_by_region_filtered["region"]
        ]

        figure = go.Figure(
            data=[
                go.Bar(
                    x=jobs_by_region_filtered["region"],
                    y=jobs_by_region_filtered["count"],
                    marker=dict(color="lightblue"),
                )
            ],
            layout=go.Layout(
                title="Number of Job Postings by Region",
                title_font=dict(size=18),
                yaxis=dict(title="Number of Job Postings"),
                hovermode="closest",
                plot_bgcolor="rgba(255, 255, 255, 1)",
            ),
        )
        return figure

      

    @app.callback(
        Output("avg-min-max-salary-region", "figure"),
        [
            Input("salary-range-slider", "value"),
            Input("job-type-checklist", "value"),
            Input("experience-level-checklist", "value"),
        ],
    )
    @cache.memoize(timeout=300)  # Cache for 5 minutes
    def update_min_max_salary_chart(
        salary_range, selected_job_types, selected_experience_levels
    ):
        """
        Update the chart to display average minimum and maximum salaries by region.

        Filters the dataset based on user-selected salary range, job types, and experience levels.
        Calculates the average minimum and maximum salaries by region and displays these as bars
        in a chart, providing insight into salary distributions.

        Parameters
        ----------
        salary_range : list of [int, int]
            A two-element list specifying the minimum and maximum salary range for filtering job postings.
        selected_job_types : list of str
            A list of job types selected by the user for filtering.
        selected_experience_levels : list of str
            A list of experience levels selected by the user for filtering.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object containing the salary range chart by region.
        """
        min_salary, max_salary = salary_range
        filtered_df = df.copy()
        filtered_df = filtered_df[
            (filtered_df["min_salary"] >= min_salary)
            & (filtered_df["max_salary"] <= max_salary)
        ]
        if selected_job_types:
            filtered_df = filtered_df[
                filtered_df["formatted_work_type"].isin(selected_job_types)
            ]
        if selected_experience_levels:
            filtered_df = filtered_df[
                filtered_df["formatted_experience_level"].isin(
                    selected_experience_levels
                )
            ]

        avg_min_max_salaries_by_region_filtered = (
            filtered_df.groupby("region")
            .agg(
                avg_min_salary=("min_salary", "mean"),
                avg_max_salary=("max_salary", "mean"),
            )
            .reset_index()
        )

        # Create the range plot with vertical bars
        figure = go.Figure()

        for i, region in enumerate(avg_min_max_salaries_by_region_filtered["region"]):
            figure.add_trace(
                go.Bar(
                    name="Salary Range",
                    x=[region],
                    y=[
                        avg_min_max_salaries_by_region_filtered["avg_max_salary"][i]
                        - avg_min_max_salaries_by_region_filtered["avg_min_salary"][i]
                    ],
                    base=avg_min_max_salaries_by_region_filtered["avg_min_salary"][i],
                    marker=dict(color="lightblue"),
                    showlegend=False,
                )
            )

        max_y_value = avg_min_max_salaries_by_region_filtered["avg_max_salary"].max()
        min_y_value = avg_min_max_salaries_by_region_filtered["avg_min_salary"].min()

        # Update layout
        figure.update_layout(
            title="Median Min and Max Salaries by Region",
            title_font=dict(size=18),
            yaxis=dict(
                title="Salary in USD", range=[min_y_value - 5000, max_y_value + 5000]
            ),
            plot_bgcolor="rgba(255, 255, 255, 1)",
        )

        return figure



    @app.callback(
        Output("state-click-info", "children"),
        [Input("job-posting", "clickData")],
        prevent_initial_call=True,
    )
    @cache.memoize(timeout=300)  # Cache for 5 minutes
    def display_clicked_region(clickData):
        """
        Display information about the clicked region on the choropleth map.

        This callback extracts the state code from the click event data on the map
        and determines the corresponding region. It then updates a text component to
        display the region of the clicked state.

        Parameters
        ----------
        clickData : dict
            Data corresponding to the click event on the map, containing the state code of the clicked state.

        Returns
        -------
        str
            A message indicating the region of the clicked state, or a default message
            if no state has been clicked yet.
        """
        if clickData is None:
            return "Click on a state to see more information here."

        state_code = clickData["points"][0]["location"]

        regions = {
            "Northeast": [
                "ME",
                "NH",
                "VT",
                "MA",
                "RI",
                "CT",
                "NY",
                "PA",
                "NJ",
                "DE",
                "MD",
            ],
            "Southeast": [
                "FL",
                "GA",
                "NC",
                "SC",
                "VA",
                "DC",
                "WV",
                "AL",
                "KY",
                "MS",
                "TN",
                "AR",
                "LA",
            ],
            "Midwest": [
                "IL",
                "IN",
                "MI",
                "OH",
                "WI",
                "IA",
                "KS",
                "MN",
                "MO",
                "NE",
                "ND",
                "SD",
            ],
            "Southwest": ["AZ", "NM", "OK", "TX"],
            "West": ["CO", "ID", "MT", "NV", "UT", "WY", "AK", "CA", "HI", "OR", "WA"],
        }

        for reg, states in regions.items():
            if state_code in states:
                region = reg
                break

        return f"Clicked Region: {region}"