# Milestone 2 Reflection

### **Implementation**

In the pursuit of developing a comprehensive dashboard, with data of U.S. job postings in LinkedIn in 2023, we implemented our dashboard with:

-   **Interactive Filters:**

    -   **State Code**: Allows filtering the data by state, with `New York (NY)` selected by default.

    -   **Minimum Salary**: A slider to set the lower bound for salary filtering, ranged from \$0 to \$100,000.

    -   **Maximum Salary**: A slider to set the upper bound for salary, ranged from \$0 to \$100,000.

    -   **Job Type**: Options to select `Full-time`, `Part-time`, and `Contract` positions. `Full-time` set as default

    -   **Experience Level**: Options for `Entry Level` and `Mid-Senior` Level.

-   **A map of the United States:** After using the filters, the map highlights the median of the maximum salary by state, with a color gradient legend indicating salary levels.

-   **Bar Charts**

    -   **Average Salary by Region**: A bar chart showing the average salary in different regions, specifically the West, Southwest, Northeast, Midwest, and Southeast.

    -   **Average Min and Max Salaries by Region**: A dual bar chart for each region showing both the average minimum and average maximum salaries side by side for comparison.

    -   **Number of Job Postings by Region**: A bar chart displaying the number of job postings in each selected region, job type and experience level.

### **Deviations from the Initial Proposal**

-   We implemented almost every part of our initial proposal, except that we were planning to incorporate more function for the map. For exampe, we planed to include a function that when we click on each state on the map we could view interested data like the highest paying position title in chosen area. But after preprocessing the data, we found that there are too many different position title and too many missing data, which make this hard to realize in our map.

-   We increased a drop-down filter for the state code so that it would work as a filter for the map. This would be more straightforward for our target users since in most case users are only interested in job market in several regions. Also we changed the chart "Number of Job Posting by Region" from a pie chart to a bar chart, for the reason that actual number of job postings could be more meaningful than the portion by region for our target users.

-   The layout of our dashboard is different to our initial proposal. One reason is that we found the map with legend on the side is taking up a larger part than we thought. Therefore, we move all the bar charts below the map. The layout looks clear and neat this way.

### Limitations

-   This dashboard works as a basic tool for analyzing U.S. job postings with interactive filters and clear visualizations that offer insights into salary ranges and job availability by region. Nonetheless, it only reflects the data in 2023 from LinkedIn. Some improvements could be made to enhance its functionality and user experience if we can have more data. Improvement may also include introducing more detailed filters such as industry-specific or role-specific selections tp provide users with more targeted information.
