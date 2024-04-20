import pandas as pd


# load the dataset
def load_data(filepath="data/processed/cleaned_job_postings.pkl"):
    """
    Load job postings data from a pickle file.

    Parameters
    ----------
    filepath : str
        The file path to the pickle file containing the job postings data.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the loaded job postings data.
    """
    df = pd.read_pickle(filepath)
    return df


# preprocess data for visualizations
def preprocess_data(df):
    """
    Preprocess job postings data for visualization.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame containing job postings data.

    Returns
    -------
    tuple of pd.DataFrame
        A tuple containing three pandas DataFrames:
        1. Jobs by region with columns ['region', 'count'].
        2. Average salary by region, sorted by average salary in descending order.
        3. Average minimum and maximum salaries by region.
    """
    jobs_by_region = df["region"].value_counts().reset_index()
    jobs_by_region.columns = ["region", "count"]

    df["avg_salary"] = df[["min_salary", "max_salary"]].mean(axis=1)
    avg_salary_by_region = df.groupby("region")["avg_salary"].mean().reset_index()
    avg_salary_by_region = avg_salary_by_region.sort_values(
        by="avg_salary", ascending=False
    )

    avg_min_max_salaries_by_region = (
        df.groupby("region")
        .agg(
            avg_min_salary=("min_salary", "mean"), avg_max_salary=("max_salary", "mean")
        )
        .reset_index()
    )

    return jobs_by_region, avg_salary_by_region, avg_min_max_salaries_by_region
