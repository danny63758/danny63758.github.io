import praw

username='danny63758'
password='HMBteam4win$'
client_id='L6Mi63ggap7A2g'
client_secret='MJViYZhfYRLhsX6jIbJ90V2HU0E'
user_agent='dc_bot3'

reddit= praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
    )

i=0
for submission in reddit.subreddit('csci040').top(limit=10):
    i+=1
    if 'joe' in submission.title.lower() or 'biden' in submission.title.lower():
        submission.upvote()
        print('upvoting')
    else:
        print('none')

