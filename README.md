# Social Sentiment Shift: The Impact of Celebrity Endorsements
## Case Study: Analyzing the Impact of Elon Musk’s Endorsement of Donald Trump on Public Sentiment


# Overview
This project investigates public sentiment towards the 2024 Presidential Election before and after celebrity endorsements. In particular, this project focuses on Elon Musk's endorsement for Donald Trump and how that's impacted the public sentiment of Reddit users, all of different political, social, and demographic groups.

## 📑 Table of Contents
1. [Objective](#objective)
2. [Goals of the Project](#GoalsoftheProject)
3. [How to Use](#HowtoUse)
4. [Technologies Used](#TechnologiesUsed)
5. [Project Features](#projectfeatures)
6. [Conclusion](#conclusion)
7. [Contributions](#contribution)
8. [Acknowledgments](#acknowledgments)



## Objective
The main objective of this research is to determine the impact of Elon Musk's endorsement of Donald Trump on public opinion, attitude, and involvement. We intend to examine how public attitudes changed before and after the endorsement by analyzing Reddit user activity, comments, and post engagement. This analysis seeks to determine how much a high-profile endorsement can impact online political conversation. This study also investigates the efficacy of applying computational tools, such as sentiment analysis and engagement tracking, to detect these changes.
More specifically, our research looks at how user sentiment, interaction patterns, and public discussions change in different subreddits that reflect a range of viewpoints and demographics. By collecting and analyzing this data, we hope to create an evidence-based understanding of how Musk's support has influenced political conversations. The insights we gain from this study could help us understand the important role that celebrity endorsements play in political campaigns and how they might shape the behavior of voters.

## Goals of the Project
Understand the impact of a high-profile celebrity endorsement on public opinion.
Identify key discussion themes and sentiment shifts across Reddit communities.
Use data analytics and visualization techniques to provide actionable insights into online political discourse.

## How to Use
1. Open up a Python supported IDE such as PyCharm or Visual Studio Code
2. Create two files: data collection program and data processing program
3. Before downloading the code, make sure to pip install the "praw", "pandas", and "nltk" packages in your terminal
4. Download 400project.py to data collect
5. Download DataProcessing.py to clean the collected data

## Technologies Used
- Python (for data collection, processing, and analysis)
- Libraries: PRAW, Pandas, Matplotlib, Seaborn, WordCloud
- JSON for data storage
- GitHub for collaboration and version control

## Project Features
Data Collection: Automated retrieval of Reddit posts and comments using the Reddit API. Data was collected across multiple subreddits, focusing on specific keywords related to the endorsement and the 2024 U.S. presidential election. (File: 400.py)

Data Cleaning: Processing and refining raw data to ensure accuracy and relevance for sentiment analysis and visualization. (File: DataProcessing.py)

Sentiment Analysis: Measuring sentiment trends across different time periods and subreddits to evaluate shifts in public opinion.

Visualization: Development of various graphs and visual tools to analyze and present the findings effectively:
- Sentiment Distribution Bar Chart (File: graph.py)
- Average Sentiment by Subreddit (File: graph2.py)
- Sentiment Trends Over Time (File: graph3.py)
- Word Cloud for Key Topics (File: graph4.py)
- Engagement Over Time (File: graph5.py)

## Conclusion

In conclusion, we explored the complex impact of Elon Musk’s endorsement of Donald Trump on Reddit’s public discourse in this study. We analyzed the sentiment and engagement patterns before and after the endorsement and we identified key shifts in user attitudes across various subreddits. This highlighted the polarized reactions that Musk’s political involvement provoked.

Our findings indicated that Musk’s endorsement significantly increased both positive and negative sentiments across different communities. This emphasizes the divisive nature of celebrity endorsements in political conversations. Politically neutral and general-interest subreddits such as r/AskMen and r/Libertarian saw the most positive reactions. This shows that Musk’s endorsement truly helped to sway the Libertarian group, which helped Trump win the election for 2025. We noticed that politically charged subreddits like r/politics and r/news exhibited the most negative responses which questioned the role of celebrities in politics, yet it wasn’t as influential when it came to the people actually changing their minds while voting. 

We also noticed how the engagement levels surged following the endorsement which illustrates the amount of influence that a celebrity endorsement can have when amplifying online discourse. Musks’s support for Trump drew more users into discussions which led to an overall rise in posts and comments overall. This study contributes to an overall understanding of how celebrity endorsements can affect public sentiment and engagement, especially in nationwide events such as the election. It also shows how useful tools such as sentiment analysis and engagement metrics are in providing insights into how influential certain figures are to the extent that they can change political perspectives. In future studies, they could extend upon this framework to analyze endorsements by other celebrities and investigate their long-term effects. They could also explore similar impacts on other social media platforms such as Twitter or YouTube. Ultimately, our study sets forth how celebrity endorsements can dramatically influence public sentiment and engagement online.


## Contributions
This was a group project, with significant contributions from all members. My primary focus areas were:

Data Collection: I developed the Python script (400.py) for fetching Reddit posts and comments using the API. This involved keyword optimization, defining timeframes, and ensuring relevant subreddit coverage.

Data Cleaning: I contributed to cleaning and preprocessing the raw data to make it suitable for sentiment analysis. This step included removing irrelevant data, formatting timestamps, and preparing datasets.

Data Visualization: I created several visualizations to highlight key findings:

- Sentiment Distribution Bar Chart (graph.py)
- Average Sentiment by Subreddit (graph2.py)
- Sentiment Trends Over Time (graph3.py)
- Word Cloud for Key Topics (graph4.py)
- Engagement Over Time (File: graph5.py)
- While I contributed significantly to most parts of the project, the Engagement Metrics Analysis (engagementmetrics.py) was primarily handled by another 
 group member.

## Acknowledgment
This project was a collaborative effort as part of our coursework, and I am grateful to my teammates for their invaluable contributions. I look forward to expanding this repository with future enhancements and related studies.

