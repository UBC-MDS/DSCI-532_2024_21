import pandas as pd

# load the dataset
def load_data(filepath="data/processed/cleaned_job_postings.csv"):
    df = pd.read_csv(filepath)
    return df

# preprocess data for visualizations
def preprocess_data(df):
    jobs_by_region = df["region"].value_counts().reset_index()
    jobs_by_region.columns = ["region", "count"]

    df["avg_salary"] = df[["min_salary", "max_salary"]].mean(axis=1)
    avg_salary_by_region = df.groupby("region")["avg_salary"].mean().reset_index()
    avg_salary_by_region = avg_salary_by_region.sort_values(by="avg_salary", ascending=False)

    avg_min_max_salaries_by_region = (
        df.groupby("region")
        .agg(avg_min_salary=("min_salary", "mean"), avg_max_salary=("max_salary", "mean"))
        .reset_index()
    )

    return jobs_by_region, avg_salary_by_region, avg_min_max_salaries_by_region