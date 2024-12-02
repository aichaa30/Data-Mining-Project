import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_before = pd.read_json("reddit_analysis/cleaned_sentiment_before.json")
data_after = pd.read_json("reddit_analysis/cleaned_sentiment_after.json")

# Check column names to find the date-related columns
print("Columns in data_before:", data_before.columns)
print("Columns in data_after:", data_after.columns)

# If 'created_date' is the date column (for example), convert it to datetime
data_before['date'] = pd.to_datetime(data_before['created_date'])
data_after['date'] = pd.to_datetime(data_after['created_date'])

# Group by date to calculate post/comment count
engagement_before = data_before.groupby(data_before['date'].dt.date).size()
engagement_after = data_after.groupby(data_after['date'].dt.date).size()

# Plot line chart
plt.plot(engagement_before.index, engagement_before, label="Before", color='blue')
plt.plot(engagement_after.index, engagement_after, label="After", color='orange')

plt.xlabel("Date")
plt.ylabel("Number of Posts/Comments")
plt.title("Engagement Over Time")
plt.legend()
plt.tight_layout()
plt.show()
