# Dashboard of LinkedIn Job Postings in the US (2023)


## Description

This project is about making a dashboard of LinkedIn job posings in the US in 2023.

Our dashboard serves as a personalized job market navigator, offering insights into job postings across the US for 2023. It provides job seekers with a clear and interactive overview of the job landscape, enabling them to filter opportunities based on salary range, job type, and regions.

## Usage

### Dashboard

Please visit the [Job Postings Dashboard](https://dsci-532-2024-21-job-postings.onrender.com/) for our dashboard!


### Developer Guide

1. Clone the repository

```bash
git clone git@github.com:UBC-MDS/DSCI-532_2024_21_Job-Postings.git
```


2. Create the virtual environment

```bash
conda env create -f environment.yml
conda activate 532_group_21
```

3. Set to `debug=True` in `src/app.py` for the development

```python
if __name__ == "__main__":
    app.run(debug=True)
```

4. Render the dashboard

```bash
python -m src.app
```


## Contributors

[@Owl64901](https://github.com/Owl64901)

[@andyzhangstat](https://github.com/andyzhangstat)

[@Prabh95](https://github.com/Prabh95)

[@sifanzzz](https://github.com/sifanzzz)


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.



## License
The Job Postings dashboard is licensed under the terms of the MIT license.

