from dash import Dash
import dash_bootstrap_components as dbc
from src.data import load_data, preprocess_data
from src.components import create_layout
from src.callbacks import register_callbacks

# Load and preprocess data
df = load_data()
jobs_by_region, avg_salary_by_region, avg_min_max_salaries_by_region = preprocess_data(df)

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Dashboard of Job Postings on LinkedIn (US, 2023)'

# Define global styles
region_colors = {
    "West": "blue",
    "Northeast": "green",
    "Southeast": "red",
    "Midwest": "pink",
    "Southwest": "orange",
}

# Set the layout of the app
app.layout = create_layout(app, df)

# Register callbacks for interactivity
register_callbacks(app, df, jobs_by_region, avg_min_max_salaries_by_region, region_colors)

# Needed for deploying
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
