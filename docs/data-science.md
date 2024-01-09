---
title: Data Science
layout: default
parent: Projects
nav_order: 4
---
# [](#Introduction)Introduction

Using the PACE project management framework, I was able to analyze data for the University of Tabuk's Applied College on behalf of the English Language Institute. For obvious confidential reasons, I am including only the code snippets in Jupyter Notebooks with general descriptions. The actual data is confidential and is not available to the public.

![](/assets/images/1683404746584.png)

# [](#Plan)Plan

Throughout the data analysis process, my goal was to understand:
*   How does attendance correlate with students' final grades?

Later, after some exploratory data analysis, it became:
*   Can clustering techniques identify distinct groups of students based on their attendance and grades?

# [](#Analyze)Analyze

The ["attendance_grades" notebook](https://github.com/perplexedstepan/data-science/blob/main/attendance_grades.ipynb) undertakes a detailed statistical analysis to understand the relationship between student attendance and final grades. Key steps included:

*   Importing necessary Python libraries like pandas, numpy, matplotlib, and sklearn for data manipulation and visualization.
*   Loading and preprocessing the dataset to ensure it is suitable for analysis.
*   Employing statistical methods and visualization techniques to explore the correlation between attendance rates and academic performance.
*   Performing regression analysis to quantify the relationship between these variables.
*   During this stage, the dataset was also cleaned by removing entries with missing data.

As mentioned earlier, however, there wasn't always an obvious relationship or correlation between the absence percentage and the final semester marks. Therefore, I asked the question about whether or not using the clustering method with machine learning would help to further understand the dataset.

# [](#Construct)Construct

The ["clustering_data" notebook](https://github.com/perplexedstepan/data-science/blob/main/clustering_data.ipynb) focuses on applying clustering techniques to the student data. The primary steps involve:

*   Importing libraries and loading the data.
*   Standardizing the dataset to make it suitable for clustering.
*   Applying clustering algorithms to segment the student population based on attendance and academic performance.
*   Analyzing the characteristics of each student cluster to draw insights.

# [](#Execute)Execute

The final implications of the data analysis include:

*   Understanding the strength and nature of the relationship between attendance and grades, which can inform educational strategies and policies.
*   Identifying distinct groups of students based on their attendance and academic performance, which can be useful for targeted interventions.
*   Providing a framework for educational institutions to utilize data analysis in enhancing student performance and engagement.
