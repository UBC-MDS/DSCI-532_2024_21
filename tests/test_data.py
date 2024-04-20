import pandas as pd
import pytest
import sys
sys.path.append('../src')
from src.data import load_data, preprocess_data

def test_load_data():
    df = load_data(filepath="data/processed/cleaned_job_postings.pkl")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_preprocess_data():
    data = {
        "region": ["East", "West", "East", "North"],
        "min_salary": [1000, 1500, 1200, 1300],
        "max_salary": [2000, 2200, 2300, 2100],
    }
    df = pd.DataFrame(data)
    jobs_by_region, avg_salary_by_region, avg_min_max_salaries_by_region = preprocess_data(df)

    # Testing if the outputs are pandas DataFrames
    assert isinstance(jobs_by_region, pd.DataFrame)
    assert isinstance(avg_salary_by_region, pd.DataFrame)
    assert isinstance(avg_min_max_salaries_by_region, pd.DataFrame)

    # Testing if the 'region' column exists in all outputs
    for output in [jobs_by_region, avg_salary_by_region, avg_min_max_salaries_by_region]:
        assert 'region' in output.columns

    # Testing specific calculated values
    assert jobs_by_region['count'].sum() == 4  # Total count of jobs
    assert avg_salary_by_region.loc[avg_salary_by_region['region'] == 'East', 'avg_salary'].values[0] == 1625.0

if __name__ == "__main__":
    pytest.main()