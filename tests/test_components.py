from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
import sys
sys.path.append('../src')
from src.components import create_layout
import pandas as pd

def create_state_info_section(df):
    state_options = [
        {"label": state, "value": state} for state in df["state_code"].unique()
    ]
    return html.Div([
        html.H4("State Info", className="section-title"),
        html.Hr(),
        html.H5("State Code"),
        dcc.Dropdown(
            id="state-dropdown",
            options=state_options,
            multi=True,
            value=None
        ),
    ], className='sidebar-section')

def test_create_state_info_section():
    df = pd.DataFrame({
        'state_code': ['CA', 'NY', 'TX'],
    })
    section = create_state_info_section(df)
    dropdown = [comp for comp in section.children if isinstance(comp, dcc.Dropdown)][0]
    assert dropdown.id == "state-dropdown"
    assert len(dropdown.options) == 3


