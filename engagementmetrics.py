import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the cleaned sentiment data from JSON files
with open('reddit_analysis/cleaned_sentiment_before.json', 'r') as before_file:
    cleaned_sentiment_before = json.load(before_file)

with open('reddit_analysis/cleaned_sentiment_after.json', 'r') as after_file:
    cleaned_sentiment_after = json.load(after_file)

df_before = pd.DataFrame(cleaned_sentiment_before)
df_after = pd.DataFrame(cleaned_sentiment_after)

# Engagement Metrics
# Count the number of posts
num_posts_before = len(df_before)
num_posts_after = len(df_after)
print(f"Number of posts before endorsement: {num_posts_before}")
print(f"Number of posts after endorsement: {num_posts_after}")

# Compute total score and total number of comments for both datasets
total_score_before = df_before['score'].sum()
total_score_after = df_after['score'].sum()

total_comments_before = df_before['num_comments'].sum()
total_comments_after = df_after['num_comments'].sum()

# Store them in a dictionary or DataFrame for easy plotting
engagement_metrics = {
    'Metric': ['Score', 'Comments'],
    'Before Endorsement': [total_score_before, total_comments_before],
    'After Endorsement': [total_score_after, total_comments_after],
}

# Convert to a pandas DataFrame
engagement_df = pd.DataFrame(engagement_metrics)

print(engagement_df)

# Bar plot for Engagement Metrics Comparison
plt.figure(figsize=(10, 6))
engagement_df.set_index('Metric').plot(kind='bar', color=['skyblue', 'salmon'], width=0.7)
plt.title('Total Engagement Metrics Before and After Endorsement')
plt.ylabel('Total Value')
plt.xlabel('Metric')
plt.xticks(rotation=0)  # Keeps the x-axis labels horizontal
plt.legend(title='Timeframe', loc='upper right')
plt.tight_layout()
plt.show()

# Convert 'created_date' to datetime format if it's not already
df_before['created_date'] = pd.to_datetime(df_before['created_date'])
df_after['created_date'] = pd.to_datetime(df_after['created_date'])

# Group by date and calculate daily total score and comments
total_engagement_before = df_before.groupby(df_before['created_date'].dt.date)[['score', 'num_comments']].sum()
total_engagement_after = df_after.groupby(df_after['created_date'].dt.date)[['score', 'num_comments']].sum()

print(f"Total engagement before endorsement: {total_engagement_before}")
print(f"Total engagement after endorsement: {total_engagement_after}")

# Plotting the total engagement trends by date
plt.figure(figsize=(12, 6))

# Plot for Score (total score over time)
plt.subplot(1, 2, 1)
plt.plot(total_engagement_before.index, total_engagement_before['score'], label='Before Endorsement', color='skyblue')
plt.plot(total_engagement_after.index, total_engagement_after['score'], label='After Endorsement', color='salmon')
plt.title('Total Score Over Time (Before vs. After)')
plt.xlabel('Date')
plt.ylabel('Total Score')
plt.legend()

# Plot for Comments (total comments over time)
plt.subplot(1, 2, 2)
plt.plot(total_engagement_before.index, total_engagement_before['num_comments'], label='Before Endorsement', color='skyblue')
plt.plot(total_engagement_after.index, total_engagement_after['num_comments'], label='After Endorsement', color='salmon')
plt.title('Total Number of Comments Over Time (Before vs. After)')
plt.xlabel('Date')
plt.ylabel('Total Number of Comments')
plt.legend()

plt.tight_layout()
plt.show()

# Additional Engagement Metrics

# Distribution of Scores and Comments
plt.figure(figsize=(14, 6))

# Distribution of Scores
plt.subplot(1, 2, 1)
plt.hist(df_before['score'], bins=30, alpha=0.7, label='Before Endorsement', color='skyblue')
plt.hist(df_after['score'], bins=30, alpha=0.7, label='After Endorsement', color='salmon')
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.legend()

# Distribution of Comments
plt.subplot(1, 2, 2)
plt.hist(df_before['num_comments'], bins=30, alpha=0.7, label='Before Endorsement', color='skyblue')
plt.hist(df_after['num_comments'], bins=30, alpha=0.7, label='After Endorsement', color='salmon')
plt.title('Distribution of Comments')
plt.xlabel('Number of Comments')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

# Engagement Metrics Over Time
# Calculate daily averages for scores and comments
daily_avg_before = df_before.groupby(df_before['created_date'].dt.date)[['score', 'num_comments']].mean()
daily_avg_after = df_after.groupby(df_after['created_date'].dt.date)[['score', 'num_comments']].mean()

# Plotting the daily averages for scores and comments
plt.figure(figsize=(14, 6))

# Average Score Over Time
plt.subplot(1, 2, 1)
plt.plot(daily_avg_before.index, daily_avg_before['score'], label='Before Endorsement', color='skyblue')
plt.plot(daily_avg_after.index, daily_avg_after['score'], label='After Endorsement', color='salmon')
plt.title('Average Score Over Time (Before vs. After)')
plt.xlabel('Date')
plt.ylabel('Average Score')
plt.legend()

# Average Number of Comments Over Time
plt.subplot(1, 2, 2)
plt.plot(daily_avg_before.index, daily_avg_before['num_comments'], label='Before Endorsement', color='skyblue')
plt.plot(daily_avg_after.index, daily_avg_after['num_comments'], label='After Endorsement', color='salmon')
plt.title('Average Number of Comments Over Time (Before vs. After)')
plt.xlabel('Date')
plt.ylabel('Average Number of Comments')
plt.legend()

plt.tight_layout()
plt.show()
