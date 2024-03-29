# Milestone 1 - Team 21

## Proposal

### 1. Motivation and purpose

Our role: Career Insights and Job Market Analytics Provider

Target audience: Job Seekers in the US

Finding suitable opportunities in the job market can be daunting for job seekers as they have to sift through large amounts of data to find suitable opportunities that match their target positions, salary expectation ranges and ideal work locations. The key challenge is the complexity and time-consuming nature of processing and understanding large amounts of job market data, which can lead to missed opportunities and unsatisfactory career decisions. Addressing this issue is crucial to enhancing job seekers' ability to quickly identify and process the most relevant job offers.

Our dashboard serves as a personalized job market navigator, offering basic insights into job postings across the US for 2023. It provides job seekers with a clear and interactive overview of the job landscape, enabling them to filter opportunities based on salary range, job type, and target regions. The regional analysis features, such as average salary by region and the proportion of job postings, equip job seekers with the knowledge to target their search geographically. By utilizing this dashboard, job seekers can efficiently have an overall understanding of their pinpoint roles, which can serve as reference for their future searching.

### 2. Description of the data


The dataset we are using is a collection of job postings from LinkedIn, which is hosted on
https://www.kaggle.com/datasets/arshkon/linkedin-job-postings.

The orginal dataset consists of 33157 rows and 28 columns providing various information about each job posting from LinkedIn. There are several interesting columns we may focus on for this visulization task, they are: `title`,`max_salary`,`min_salary`, `pay_period`, `formatted_work_type`,`location`, `remote_allowed`,`sponsored`,`formatted_experience_level`. 

#### Columns:

Some columns in orginal dataset contain a lot of missing data, so we need to preprocess the data before feeding it to the dashboard. After removing the missing data, the final dataset we will work on is approximately 11100 rows and 10 columns. 

The dataset contains various categorical variables:
- `pay_period`: Indicates how often salary is paid (Hourly, Monthly, Yearly).
- `formatted_work_type`: Categorizes the type of work arrangement (Full-time, Part-time, Contract).
- `location`: Specifies the geographic location of the job (e.g., New York, NY; Bellevue, WA; Oakland, CA).
- `formatted_experience_level`: Represents the required level of job experience (entry, associate, executive, etc.).
- `sponsored`: Indicates whether the job listing is sponsored or promoted.
- `remote_allowed`: Signals whether remote work is allowed for the job.


#### Salary/Type/Location Distribution and More:

This dataset contains the work salary information which includes the maximum salary and minumum salary. This dataset also provides information on the distribution of work types. It shows the number of job postings categorized as full-time, contract, or other. Additionally, it provides distribution for job locations, with a focus on the United States. Besides, This dataset contains has remote type, sponsored type, work type, experience level for us to explore.


#### Insights:

This dataset offers valuable insights into the job market, including salary trends, distribution of work types, and job locations. Each sample includes details such as job title, company, description, salary, pay period, work type, and location. It can be utilized for analysis purposes such as identifying high-demand job sectors, understanding salary expectations, and exploring geographical job trends.








### 3. Research questions

Our easy to use dashboard can help people from different fields and expertise and below are some of the user personas:

**a) Jacob - The Recent College Graduate**

Jacob is a recent computer science graduate looking for a full-time entry-level software development position in the technology sector. Eager to find a job that aligns with his skills and pays a competitive salary, Jacob uses the dashboard's filters to set a minimum salary expectation and select full-time job postings. By focusing on states in the West and Northeast regions, known for their tech industries, he can quickly visualize which states have the highest-paying jobs that match his criteria. Jacob uses the color-coded map to identify hotspots for tech jobs and uses the average salary by region bar chart to decide where to concentrate his applications.

**b) Angela - The Career Advisor**

Angela is a career advisor at a large university, assisting students and alumni in navigating their job search. She utilizes the dashboard to prepare for advising sessions by setting various filters to match the diverse needs of her clientele. With the dashboard, Angela can compare the average salaries and job distribution in different regions to guide students on where they might want to relocate for better opportunities. She pays particular attention to the pie chart showing the proportion of job postings by region to inform students about market saturation and potential competition in their fields.

**c) Carlos - The Human Resources Analyst**

Carlos works as a human resources analyst for a multinational corporation and is responsible for providing insights on the competitive landscape of salaries and job opportunities. He leverages the dashboard's dynamic features to tailor searches for different categories of corporate jobs across various experience levels. By adjusting the salary range sliders, Carlos can analyze the market for mid-senior level positions in the Southeast and Midwest regions, where his company has a significant presence. The clickable map feature aids Carlos in identifying which states may require salary adjustments to attract top talent, and the real-time updating charts help him in preparing reports for the executive team on regional compensation trends.

### 4. App sketch and description

![sketch](../img/sketch.png)

The app provides a user-friendly dashboard to explore U.S. job postings, featuring a dynamic map and comprehensive filtering options. Users can adjust salary ranges through sliders and specify the type of job and experience level via checkboxes to tailor the job search. The map offers a color-coded view of job postings by region, with a clickable feature for pinpointing the highest-paying opportunities in each state. On the right side, bar and pie charts display the average salary by region and the proportion of job postings by region, respectively, updating in real-time to reflect changes made through the filters. This interactive platform is designed for simplicity, ensuring that users can seamlessly navigate through different data visualizations to gain insights into the U.S. job market.
