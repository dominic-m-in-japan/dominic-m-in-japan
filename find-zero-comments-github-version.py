import praw
from datetime import datetime, timedelta

# --- Configuration ---
CLIENT_ID = "make your own"
CLIENT_SECRET = "make your own"
USER_AGENT = "zero_comment_finder:v1.0 (by u/make your own)"
SUBREDDIT_NAME = "make your own"  # change to a specific subreddit if desired
LIMIT = 1000  # how many posts to check

# --- Setup ---
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

cutoff = datetime.utcnow() - timedelta(days=30)

print(f"Searching r/{SUBREDDIT_NAME} for posts from the last 30 days with zero comments...\n")

for submission in reddit.subreddit(SUBREDDIT_NAME).new(limit=LIMIT):
    post_time = datetime.utcfromtimestamp(submission.created_utc)
    if post_time > cutoff and submission.num_comments == 0:
        print(f"[{post_time.strftime('%Y-%m-%d')}] {submission.title}")
        print(f"  {submission.url}\n")
