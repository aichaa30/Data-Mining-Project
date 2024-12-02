import nltk
import pandas as pd
import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer


# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Part 1: Load JSON Files
with open("reddit_analysis/before_endorsement.json", "r") as before_file:
    data_before = json.load(before_file)

with open("reddit_analysis/after_endorsement.json", "r") as after_file:
    data_after = json.load(after_file)



# Part 2: Define Cleaning Functions
def clean_text(text):
    """Cleans and normalizes text by removing URLs, special characters, and stopwords."""
    text = re.sub(r"(http|https):\/\/\S+|www\.\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize text
    tokens = [word for word in tokens if word not in stopwords.words("english")]  # Remove stopwords
    return " ".join(tokens)

def clean_data(dataset):
    """Applies text cleaning to titles and comments in the dataset."""
    for item in dataset:
        if "title" in item:
            item["cleaned_title"] = clean_text(item["title"])
        else:
            item["cleaned_title"] = ""

        if "comments" in item and isinstance(item["comments"], list):
            item["cleaned_comments"] = [clean_text(comment) for comment in item["comments"]]
        else:
            item["cleaned_comments"] = []
    return dataset

# Part 3: Sentiment Analysis with Neutral Detection

def add_sentiment_with_classification(dataset, neutral_threshold=0.05):
    """Adds sentiment scores, flags neutral sentiments, and classifies sentiments."""
    for item in dataset:
        # Sentiment for title
        if "cleaned_title" in item:
            title_sentiment = sia.polarity_scores(item["cleaned_title"])["compound"]
            item["title_sentiment"] = title_sentiment
            item["title_is_neutral"] = abs(title_sentiment) <= neutral_threshold

            # Classify sentiment
            if title_sentiment > neutral_threshold:
                item["title_sentiment_class"] = "positive"
            elif title_sentiment < -neutral_threshold:
                item["title_sentiment_class"] = "negative"
            else:
                item["title_sentiment_class"] = "neutral"

        # Sentiment for comments
        if "cleaned_comments" in item and isinstance(item["cleaned_comments"], list):
            comment_sentiments = [sia.polarity_scores(comment)["compound"] for comment in item["cleaned_comments"]]
            if comment_sentiments:
                avg_comment_sentiment = sum(comment_sentiments) / len(comment_sentiments)
                item["average_comment_sentiment"] = avg_comment_sentiment
                item["comments_are_neutral"] = all(abs(score) <= neutral_threshold for score in comment_sentiments)

                # Classify average comment sentiment
                if avg_comment_sentiment > neutral_threshold:
                    item["comments_sentiment_class"] = "positive"
                elif avg_comment_sentiment < -neutral_threshold:
                    item["comments_sentiment_class"] = "negative"
                else:
                    item["comments_sentiment_class"] = "neutral"
            else:
                item["average_comment_sentiment"] = None
                item["comments_are_neutral"] = False
                item["comments_sentiment_class"] = "neutral"
    return dataset

# Part 4: Process Data
# Clean the data
data_before_cleaned = clean_data(data_before)
data_after_cleaned = clean_data(data_after)

# Add sentiment analysis
data_before_sentiment = add_sentiment_with_classification(data_before_cleaned)
data_after_sentiment = add_sentiment_with_classification(data_after_cleaned)

# Part 5: Save Combined Files
with open("reddit_analysis/cleaned_sentiment_before.json", "w") as before_file:
    json.dump(data_before_sentiment, before_file, indent=4)

with open("reddit_analysis/cleaned_sentiment_after.json", "w") as after_file:
    json.dump(data_after_sentiment, after_file, indent=4)

print("Cleaned and sentiment-analyzed data saved successfully.")

# Convert to pandas DataFrame
df_before = pd.DataFrame(data_before_sentiment)
df_after = pd.DataFrame(data_after_sentiment)
print(df_before.head())  # View a snapshot of the data are orgonized
print(df_before.columns)
print(df_after.columns)
# Group data by subreddit and calculate average sentiment
if "subreddit" in df_before.columns:
    before_sentiment_by_subreddit = df_before.groupby("subreddit")["title_sentiment"].mean()
    after_sentiment_by_subreddit = df_after.groupby("subreddit")["title_sentiment"].mean()

    print("Before Endorsement Sentiment by Subreddit:")
    print(before_sentiment_by_subreddit)

    print("\nAfter Endorsement Sentiment by Subreddit:")
    print(after_sentiment_by_subreddit)
else:
    print("The 'subreddit' column is missing. Ensure the input data includes subreddit information.")

