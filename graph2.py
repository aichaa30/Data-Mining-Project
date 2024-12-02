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
print(type(df_before))  # Check the type
print(df_before.head())  # Preview the data (if it is a DataFrame)
df_after = pd.DataFrame(data_after_sentiment)



# Verify data structure
print("Columns in df_before:", df_before.columns)
print("Columns in df_after:", df_after.columns)

# Ensure date column is parsed as datetime if it exists
if 'date' in df_before.columns:
    df_before['date'] = pd.to_datetime(df_before['date'])
if 'date' in df_after.columns:
    df_after['date'] = pd.to_datetime(df_after['date'])

print("Subreddits in 'before':", df_before['subreddit'].unique())
askmen_before = df_before[df_before['subreddit'] == 'askmen']
print(askmen_before[['title_sentiment', 'subreddit']])

# 2. Average Sentiment by Subreddit
def plot_sentiment_by_subreddit():
    if "subreddit" in df_before.columns:
        # Group data by subreddit and calculate average sentiment
        before_sentiment_by_subreddit = df_before.groupby("subreddit")["title_sentiment"].mean()
        after_sentiment_by_subreddit = df_after.groupby("subreddit")["title_sentiment"].mean()

        # Align the indices of both series
        all_subreddits = before_sentiment_by_subreddit.index.union(after_sentiment_by_subreddit.index)
        before_sentiment_by_subreddit = before_sentiment_by_subreddit.reindex(all_subreddits, fill_value=0)
        after_sentiment_by_subreddit = after_sentiment_by_subreddit.reindex(all_subreddits, fill_value=0)

        # Bar plot
        x = range(len(all_subreddits))

        plt.bar(x, before_sentiment_by_subreddit, width=0.4, label='Before Endorsement', color='blue', align='center')
        plt.bar([i + 0.4 for i in x], after_sentiment_by_subreddit, width=0.4, label='After Endorsement', color='orange', align='center')

        plt.xlabel('Subreddit')
        plt.ylabel('Average Sentiment Score')
        plt.title('Average Sentiment by Subreddit')
        plt.xticks([i + 0.2 for i in x], all_subreddits, rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("The 'subreddit' column is missing. Cannot plot sentiment by subreddit.")
plot_sentiment_by_subreddit()
