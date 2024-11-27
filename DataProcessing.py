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

# Part 3: Clean the Data
data_before_cleaned = clean_data(data_before)
data_after_cleaned = clean_data(data_after)
# Convert to pandas DataFrame
df_before = pd.DataFrame(data_before)
df_after = pd.DataFrame(data_after)

print(df_before.head())  # View a snapshot of the data are orgonized



#Part2: Data cleaning and processing. We will use text normalization and tokenization.
#Define a text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize text
    tokens = [word for word in tokens if word not in stopwords.words("english")]  # Remove stopwords
    return " ".join(tokens)

# Apply cleaning function to titles and comments
def clean_data(dataset):
    for item in dataset:
        item["cleaned_title"] = clean_text(item["title"])
        item["cleaned_comments"] = [clean_text(comment) for comment in item["comments"]]
    return dataset

# Clean the data
data_before_cleaned = clean_data(data_before)
data_after_cleaned = clean_data(data_after)

# Save cleaned data to JSON files
with open("reddit_analysis/cleaned_before_endorsement.json", "w") as before_file:
    json.dump(data_before_cleaned, before_file, indent=4)

with open("reddit_analysis/cleaned_after_endorsement.json", "w") as after_file:
    json.dump(data_after_cleaned, after_file, indent=4)

print("Cleaned data saved successfully.")

#print(stopwords.words('english')[:10])  # Should output the first 10 stopwords to see if the import nltk stopwords works
# Save cleaned data to new JSON files
with open("reddit_analysis/cleaned_before_endorsement.json", "w") as before_cleaned_file:
    json.dump(data_before_cleaned, before_cleaned_file, indent=4)

with open("reddit_analysis/cleaned_after_endorsement.json", "w") as after_cleaned_file:
    json.dump(data_after_cleaned, after_cleaned_file, indent=4)

print("Cleaned data saved successfully.")

# Part 4: Perform Sentiment Analysis
def add_sentiment(dataset):
    """Adds sentiment scores for cleaned titles and comments."""
    for item in dataset:
        # Sentiment for title
        if "cleaned_title" in item:
            title_sentiment = sia.polarity_scores(item["cleaned_title"])
            item["title_sentiment"] = title_sentiment["compound"]

        # Sentiment for comments
        if "cleaned_comments" in item and isinstance(item["cleaned_comments"], list):
            comment_sentiments = [sia.polarity_scores(comment)["compound"] for comment in item["cleaned_comments"]]
            if comment_sentiments:
                item["average_comment_sentiment"] = sum(comment_sentiments) / len(comment_sentiments)
            else:
                item["average_comment_sentiment"] = None
    return dataset

# Apply Sentiment Analysis
data_before_sentiment = add_sentiment(data_before_cleaned)
data_after_sentiment = add_sentiment(data_after_cleaned)

# Save sentiment analysis results to new JSON files
with open("reddit_analysis/sentiment_before_endorsement.json", "w") as before_sentiment_file:
    json.dump(data_before_sentiment, before_sentiment_file, indent=4)

with open("reddit_analysis/sentiment_after_endorsement.json", "w") as after_sentiment_file:
    json.dump(data_after_sentiment, after_sentiment_file, indent=4)

print("Sentiment analysis results saved successfully.")

# Group data by subreddit and calculate average sentiment
#Analyze demographic
before_sentiment_by_subreddit = df_before.groupby("subreddit")["title_sentiment"].mean()
after_sentiment_by_subreddit = df_after.groupby("subreddit")["title_sentiment"].mean()

print("Before Endorsement Sentiment by Subreddit:")
print(before_sentiment_by_subreddit)

print("\nAfter Endorsement Sentiment by Subreddit:")
print(after_sentiment_by_subreddit)
