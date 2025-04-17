# this is the code I used to get data from Reddit about the word "carry"
# for now, this will just get post titles and text (if there is any)
# I will put a more extended script that also pulls comments later

#import modules: reddit API and pandas
import praw
import pandas as pd

# Fill in with your credentials
reddit = praw.Reddit(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    user_agent='carry_data_test',
    username='reddit_username',
    password='reddit_password'
)

# put the subreddit you're searching
subreddit = reddit.subreddit('guns')

#make an empty list
posts = []
for post in subreddit.search("carry", limit=100):
    posts.append({
        'title': post.title,
        'selftext': post.selftext,
        'author': str(post.author),
        'score': post.score,
        'num_comments': post.num_comments,
        'created_utc': post.created_utc,
        'permalink': f"https://www.reddit.com{post.permalink}"
    })

# Convert to DataFrame
df = pd.DataFrame(posts)
df.to_csv('praw_carry_posts.csv', index=False)
print("Saved praw_carry_posts.csv")
