import praw

username='danny63758'
password='HMBteam4win$'
client_id='M6p8A6v1kkg_fg'
client_secret='Ie9eYZPOzsH7mCAUHE5hK3wStRA'
user_agent='dc_bot1'

reddit= praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
    )

i=0
for submission in reddit.subreddit('csci040').top(limit=300):
    i+=1
    if 'joe' in submission.title.lower() or 'biden' in submission.title.lower():
        submission.upvote()
        print('upvoting')
    else:
        print('none')
