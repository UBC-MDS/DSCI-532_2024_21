from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

def register_callbacks(app, df, jobs_by_region, avg_salary_by_region, avg_min_max_salaries_by_region, region_colors):
    
    @app.callback(
        Output("job-posting", "figure"),
        [Input("state-dropdown", "value")]
    )
    def update_graph(selected_states):
        df_filtered = df[df['state_code'].isin(selected_states)]
        median_salary = df_filtered.groupby('state_code')['max_salary'].median().reset_index()

        fig = px.choropleth(median_salary, locations="state_code", color="max_salary",
                            locationmode="USA-states", scope="usa",
                            color_continuous_scale='Viridis',
                            range_color=(median_salary['max_salary'].min(), median_salary['max_salary'].max()),
                            labels={'max_salary': 'Median of Max Salary'}, title='Median of Max Salary by State in U.S.')
        fig.update_layout(mapbox_style="carto-positron")

        return fig



    @app.callback(
        Output("jobs-by-region-bar-chart", "figure"),
        [
            Input("min-salary-slider", "value"),
            Input("max-salary-slider", "value"),
            Input("job-type-checklist", "value"),
            Input("experience-level-checklist", "value"),
        ],
    )
    def update_bar_chart(min_salary, max_salary, selected_job_types, selected_experience_levels):
        filtered_df = df.copy()
        filtered_df = filtered_df[(filtered_df["min_salary"] >= min_salary) & (filtered_df["max_salary"] <= max_salary)]
        if selected_job_types:
            filtered_df = filtered_df[filtered_df["formatted_work_type"].isin(selected_job_types)]
        if selected_experience_levels:
            filtered_df = filtered_df[filtered_df["formatted_experience_level"].isin(selected_experience_levels)]
        
        jobs_by_region_filtered = filtered_df["region"].value_counts().reset_index()
        jobs_by_region_filtered.columns = ["region", "count"]
        bar_colors = [region_colors.get(region, "gray") for region in jobs_by_region_filtered["region"]]

        figure = go.Figure(
            data=[
                go.Bar(
                    x=jobs_by_region_filtered["region"],
                    y=jobs_by_region_filtered["count"],
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



    @app.callback(
        Output("average-salary-region", "figure"),
        [
            Input("min-salary-slider", "value"),
            Input("max-salary-slider", "value"),
            Input("job-type-checklist", "value"),
            Input("experience-level-checklist", "value"),
        ],
    )
    def update_avg_salary_chart(min_salary, max_salary, selected_job_types, selected_experience_levels):
        filtered_df = df.copy()
        filtered_df = filtered_df[(filtered_df["min_salary"] >= min_salary) & (filtered_df["max_salary"] <= max_salary)]
        if selected_job_types:
            filtered_df = filtered_df[filtered_df["formatted_work_type"].isin(selected_job_types)]
        if selected_experience_levels:
            filtered_df = filtered_df[filtered_df["formatted_experience_level"].isin(selected_experience_levels)]
        
        filtered_df["avg_salary"] = filtered_df[["min_salary", "max_salary"]].mean(axis=1)
        avg_salary_by_region_filtered = filtered_df.groupby("region")["avg_salary"].mean().reset_index()
        avg_salary_by_region_filtered = avg_salary_by_region_filtered.sort_values(by="avg_salary", ascending=False)
        
        bar_colors_avg_sal = [region_colors[region] for region in avg_salary_by_region_filtered["region"]]
        
        figure = go.Figure()
        figure.add_trace(
            go.Bar(
                x=avg_salary_by_region_filtered["region"],
                y=avg_salary_by_region_filtered["avg_salary"],
                marker=dict(color=bar_colors_avg_sal),
            )
        )
        figure.update_layout(
            title="Average Salary by Region",
            xaxis_title="Region",
            yaxis_title="Average Salary in USD",
            template="plotly_white",
        )
        return figure



    @app.callback(
        Output("avg-min-max-salary-region", "figure"),
        [
            Input("min-salary-slider", "value"),
            Input("max-salary-slider", "value"),
            Input("job-type-checklist", "value"),
            Input("experience-level-checklist", "value"),
        ],
    )
    def update_min_max_salary_chart(min_salary, max_salary, selected_job_types, selected_experience_levels):
        filtered_df = df.copy()
        filtered_df = filtered_df[(filtered_df["min_salary"] >= min_salary) & (filtered_df["max_salary"] <= max_salary)]
        if selected_job_types:
            filtered_df = filtered_df[filtered_df["formatted_work_type"].isin(selected_job_types)]
        if selected_experience_levels:
            filtered_df = filtered_df[filtered_df["formatted_experience_level"].isin(selected_experience_levels)]
        
        avg_min_max_salaries_by_region_filtered = filtered_df.groupby("region").agg(avg_min_salary=("min_salary", "mean"), avg_max_salary=("max_salary", "mean")).reset_index()

        figure = go.Figure(
            data=[
                go.Bar(
                    name="Avg Min Salary", 
                    x=avg_min_max_salaries_by_region_filtered["region"], 
                    y=avg_min_max_salaries_by_region_filtered["avg_min_salary"],
                ),
                go.Bar(
                    name="Avg Max Salary", 
                    x=avg_min_max_salaries_by_region_filtered["region"], 
                    y=avg_min_max_salaries_by_region_filtered["avg_max_salary"],
                ),
            ]
        )
        figure.update_layout(
            barmode="group", 
            title="Average Min and Max Salaries by Region", 
            xaxis_title="Region", 
            yaxis_title="Average Salary in USD",
        )
        return figure



