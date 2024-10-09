import pandas as pd
import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT')
)

top_post = reddit.subreddit('MachineLearning').top(limit=10)
for posts in top_post:
    print(posts.title)