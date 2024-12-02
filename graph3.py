import pandas as pd
import matplotlib.pyplot as plt
import json


# Load the data
with open("reddit_analysis/cleaned_sentiment_before.json", "r") as before_file:
    data_before_sentiment = json.load(before_file)

with open("reddit_analysis/cleaned_sentiment_after.json", "r") as after_file:
    data_after_sentiment = json.load(after_file)

# Convert to pandas DataFrame
df_before = pd.DataFrame(data_before_sentiment)
df_after = pd.DataFrame(data_after_sentiment)

# Verify data structure
print("Columns in df_before:", df_before.columns)
print("Columns in df_after:", df_after.columns)

# Ensure the created_date column is parsed as datetime if it exists
if 'created_date' in df_before.columns:
    df_before['created_date'] = pd.to_datetime(df_before['created_date'])
if 'created_date' in df_after.columns:
    df_after['created_date'] = pd.to_datetime(df_after['created_date'])

# 3. Sentiment Trends Over Time
def plot_sentiment_trends_over_time():
    if 'created_date' in df_before.columns and 'created_date' in df_after.columns:
        before_sentiment_trend = df_before.groupby(df_before['created_date'].dt.date)['title_sentiment'].mean()
        after_sentiment_trend = df_after.groupby(df_after['created_date'].dt.date)['title_sentiment'].mean()

        plt.plot(before_sentiment_trend.index, before_sentiment_trend, label='Before Endorsement', color='blue')
        plt.plot(after_sentiment_trend.index, after_sentiment_trend, label='After Endorsement', color='orange')

        plt.xlabel('Date')
        plt.ylabel('Average Sentiment Score')
        plt.title('Sentiment Trends Over Time')
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("The 'created_date' column is missing. Cannot plot sentiment trends over time.")

plot_sentiment_trends_over_time()
