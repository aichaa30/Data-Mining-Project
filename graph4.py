import pandas as pd
import matplotlib.pyplot as plt
import json
from wordcloud import WordCloud

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

# 4. Word Cloud: Key Topics
def plot_word_clouds():
    before_text = ' '.join(df_before['cleaned_title'])
    after_text = ' '.join(df_after['cleaned_title'])

    wordcloud_before = WordCloud(width=800, height=400, background_color='white').generate(before_text)
    wordcloud_after = WordCloud(width=800, height=400, background_color='white').generate(after_text)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(wordcloud_before, interpolation='bilinear')
    plt.title('Word Cloud Before Endorsement')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(wordcloud_after, interpolation='bilinear')
    plt.title('Word Cloud After Endorsement')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
plot_word_clouds()