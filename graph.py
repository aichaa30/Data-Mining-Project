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

# Ensure date column is parsed as datetime if it exists
if 'date' in df_before.columns:
    df_before['date'] = pd.to_datetime(df_before['date'])
if 'date' in df_after.columns:
    df_after['date'] = pd.to_datetime(df_after['date'])



# 1. Sentiment Distribution Bar Chart
def plot_sentiment_distribution():
    before_sentiment_counts = df_before['title_sentiment_class'].value_counts()
    after_sentiment_counts = df_after['title_sentiment_class'].value_counts()

    labels = before_sentiment_counts.index
    x = range(len(labels))

    plt.bar(x, before_sentiment_counts, width=0.4, label='Before Endorsement', color='blue', align='center')
    plt.bar([i + 0.4 for i in x], after_sentiment_counts, width=0.4, label='After Endorsement', color='orange', align='center')

    plt.xlabel('Sentiment Class')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution Before and After Endorsement')
    plt.xticks([i + 0.2 for i in x], labels)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Call the functions with pauses between them
plot_sentiment_distribution()




