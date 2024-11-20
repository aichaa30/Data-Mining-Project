from datetime import datetime, timedelta
import praw
reddit = praw.Reddit(
    client_id= "m5ioiKMETwTaUOnPmBhDQw",
    client_secret="0gUZLUpcF4UmudcnAtNndmL6M0t2Pw",
    password="Tibile2009!",
    user_agent="CIS 400",
    username="Suitable_Bus_1876",)


# Define timeframes (Unix timestamps)
endorsement_date = datetime(2024, 1, 1)  # Example endorsement date
before_start = int((endorsement_date - timedelta(days=30)).timestamp())
before_end = int(endorsement_date.timestamp())
after_start = int(endorsement_date.timestamp())
after_end = int((endorsement_date + timedelta(days=30)).timestamp())

# Search posts in relevant subreddit (before endorsement)
subreddit = reddit.subreddit("politics")
for post in subreddit.search("Elon Musk endorsement", sort="new", time_filter="month"):
    print(f"A-Title: {post.title}, B-Score: {post.score}, C-Numcomments: {post.num_comments}, D-Created_utc: {post.created_utc}")

    post.comments.replace_more(limit=0)
    for comment in post.comments.list():
        print(f"  Comment by {comment.author}: {comment.body} - Score: {comment.score}")
