import praw
import os

def main():
    client_id = os.environ['REDDIT_CLIENT_ID']
    client_secret = os.environ['REDDIT_CLIENT_SECRET']
    user_agent = 'script by /u/citostyle'

    subreddit_name = 'relationships'
    submissions = extract_submissions(client_id, client_secret, user_agent, subreddit_name)
    print(submissions)
    #print(len(submissions))

def extract_submissions(client_id, client_secret, user_agent, subreddit_name):
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    subreddit = reddit.subreddit(subreddit_name)
    submissions = [{'id': s.id, 'title': s.title, 'upvotes': s.ups, 'downvotes': s.downs, 'href': s.permalink, 'number_of_comments': s.num_comments, 'content': s.selftext} for s in subreddit.hot(limit=None)]
    return submissions


main()
    
