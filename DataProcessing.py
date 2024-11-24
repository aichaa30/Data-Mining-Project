

import nltk
import pandas as pd #data manipulation and analysis
import json #files access
import re #regularexpression
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize



#Part1: Loading JSON files
with open("reddit_analysis/before_endorsement.json", "r") as before_file: #we have reddit_analysis/ because we saved the files in a directory  so we need to get into the directory first then egt to the foles themselves.
    data_before = json.load(before_file)

with open("reddit_analysis/after_endorsement.json", "r") as after_file:
    data_after = json.load(after_file)

# Convert to pandas DataFrame
df_before = pd.DataFrame(data_before)
df_after = pd.DataFrame(data_after)

print(df_before.head())  # View a snapshot of the data are orgonized


#print(stopwords.words('english')[:10])  # Should output the first 10 stopwords


#Part2: Data cleaning and processing. We will use text normalization and tokenization.
# Define a text cleaning function
"""def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize text
    tokens = [word for word in tokens if word not in stopwords.words("english")]  # Remove stopwords
    return " ".join(tokens)

# Apply cleaning function to titles and comments
df_before["cleaned_title"] = df_before["title"].apply(clean_text)
df_before["cleaned_comments"] = df_before["comments"].apply(lambda x: [clean_text(comment) for comment in x])

df_after["cleaned_title"] = df_after["title"].apply(clean_text)
df_after["cleaned_comments"] = df_after["comments"].apply(lambda x: [clean_text(comment) for comment in x])"""