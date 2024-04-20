# Milestone 4 Reflection

In Milestone 4, we make some changes to our dashboard, including:

## Major changes

-   Map click = select in drop-down.

    When we click on a certain state on the map, the state code filter on the side will be synchronized.

    When using the lasso select tool to choose a group of states on the map, the state code filter on the side will also be synchronized.

-   Switch bar charts for a ranged chart. (or other similar clarification)

-   Get rid of the bottom left bar chart since the average of the min and max is not that intuitive and will already be covered by the ranged charts

-   Separate the filter to two parts, the upper state code filter is used for the map, and the lower region filter is used for the bar charts

## Minor changes

-   Remove map title because info already in colorbar

-   Separate widgets into "region"info" at the bottom and "state info" at the top

-   Change bars to be less colorful. Consider just using the sidebar color for all of them

-   Fix the crowded numbers issue in salary range slider

-   Change bar chart color theme to make the dashboard more consistent

## Challenges and Limitations

There are still some challenges we could not overcome in this milestone.

Firstly, although we added the function of "Map click = select", we could not achieve multiple selection by clicking at the same time. The problem seems to lie in not being able to detect the second click, but we failed to fix this at this moment. And the filter can only control the map, instead of linking to all the bar charts below.

Secondly, as suggested by peers to add an industry-specific filter to allow job seekers to tailor the job search to their field of expertise, we, although believe this could be a very useful function of our dashboard, could not complete this due to the lack in relative data. At the mean time, we considered using positions instead of industry information from our raw data, but since there are too many unique values, we could not find a good method to categorize the positions.

If we can fix these beforementioned challenges, the dash board can have more interactive. Also, if we have more data regarding industry and position categories, we can add more filters and charts for the users to get more customized visual outputs.
