import pandas as pd
import matplotlib.pyplot as plt
import json
# Assuming df_before and df_after are pandas DataFrames containing the cleaned data
import json

# Load the cleaned sentiment data from JSON files
with open('reddit_analysis/cleaned_sentiment_before.json', 'r') as before_file:
    cleaned_sentiment_before = json.load(before_file)

with open('reddit_analysis/cleaned_sentiment_after.json', 'r') as after_file:
    cleaned_sentiment_after = json.load(after_file)

df_before = pd.DataFrame(cleaned_sentiment_before)
df_after = pd.DataFrame(cleaned_sentiment_after)
# Compute average score and average number of comments for both datasets
avg_score_before = df_before['score'].mean()
avg_score_after = df_after['score'].mean()

avg_comments_before = df_before['num_comments'].mean()
avg_comments_after = df_after['num_comments'].mean()

# Store them in a dictionary or DataFrame for easy plotting
engagement_metrics = {
    'Metric': ['Score', 'Comments'],
    'Before Endorsement': [avg_score_before, avg_comments_before],
    'After Endorsement': [avg_score_after, avg_comments_after],
}

# Convert to a pandas DataFrame
engagement_df = pd.DataFrame(engagement_metrics)

print(engagement_df)


# Bar plot for Engagement Metrics Comparison
plt.figure(figsize=(10, 6))
engagement_df.set_index('Metric').plot(kind='bar', color=['skyblue', 'salmon'], width=0.7)
plt.title('Engagement Metrics Before and After Endorsement')
plt.ylabel('Average Value')
plt.xlabel('Metric')
plt.xticks(rotation=0)  # Keeps the x-axis labels horizontal
plt.legend(title='Timeframe', loc='upper right')
plt.tight_layout()
plt.show()
