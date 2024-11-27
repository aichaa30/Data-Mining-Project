from datetime import datetime, timedelta
import praw
import json
import os

# Configure Reddit API client
reddit = praw.Reddit(
    client_id="m5ioiKMETwTaUOnPmBhDQw",
    client_secret="0gUZLUpcF4UmudcnAtNndmL6M0t2Pw",
    password="Tibile2009!",
    user_agent="CIS 400",
    username="Suitable_Bus_1876",
)

# Define endorsement date and expanded timeframes
endorsement_date = datetime(2024, 7, 13)  # Elon Musk endorses Trump
before_start = int((endorsement_date - timedelta(days=90)).timestamp())  # 3 months before
before_end = int(endorsement_date.timestamp())  # End date of before timeframe
after_start = int(endorsement_date.timestamp())  # Start date of after timeframe
after_end = int((endorsement_date + timedelta(days=90)).timestamp())  # 3 months after

# Subreddits to analyze
subreddits = [
    "politics",
    "Conservative",
    "liberal",
    "Libertarian",
    "AskWomen",
    "AskMen",  # Added male demographic subreddit
    "news",
    "PoliticalDiscussion",
]

# Search keywords to broaden the search
search_keywords = [
    "Elon Musk endorsement",
    "Musk endorses Trump",
    "Musk supports Trump",
    "Trump and Musk",
    "2024 election",
    "Trump campaign 2024",
    "Elon Musk politics",
]


# Function to fetch posts
def fetch_posts(subreddit_name, keywords, time_start, time_end):
    subreddit = reddit.subreddit(subreddit_name)
    results = []
    for keyword in keywords:
        for post in subreddit.search(keyword, sort="new", time_filter="all"):
            if time_start <= post.created_utc <= time_end:
                readable_date = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                post_data = {
                    "subreddit": subreddit_name,
                    "title": post.title,
                    "score": post.score,
                    "num_comments": post.num_comments,
                    "created_utc": post.created_utc,
                    "created_date": readable_date,  # Add readable date
                    "id": post.id,
                    "comments": [],
                }
                # Fetch comments
                try:
                    post.comments.replace_more(limit=0)
                    for comment in post.comments.list():
                        if hasattr(comment, "body"):
                            post_data["comments"].append(comment.body)
                except Exception as e:
                    print(f"Error fetching comments for post {post.id}: {e}")
                results.append(post_data)
    return results


# Collect data for all subreddits
data_before = []
data_after = []

for subreddit in subreddits:
    # Data before the endorsement
    print(f"Fetching data BEFORE the endorsement for subreddit: {subreddit}")
    before_data = fetch_posts(subreddit, search_keywords, before_start, before_end)
    data_before.extend(before_data)

    # Data after the endorsement
    print(f"Fetching data AFTER the endorsement for subreddit: {subreddit}")
    after_data = fetch_posts(subreddit, search_keywords, after_start, after_end)
    data_after.extend(after_data)

# Save the results to JSON files
output_dir = "reddit_analysis"
os.makedirs(output_dir, exist_ok=True)

before_file_path = os.path.join(output_dir, "before_endorsement.json")
after_file_path = os.path.join(output_dir, "after_endorsement.json")

with open(before_file_path, "w") as before_file:
    json.dump(data_before, before_file, indent=4)

with open(after_file_path, "w") as after_file:
    json.dump(data_after, after_file, indent=4)

print(f"Data collection completed. Files saved:")
print(f"- Before endorsement data: {os.path.abspath(before_file_path)}")
print(f"- After endorsement data: {os.path.abspath(after_file_path)}")
