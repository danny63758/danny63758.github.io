import praw

username='danny63758'
password='HMBteam4win$'
client_id='I2t3wYrdikfY9g'
client_secret='ewDQlThN5oyNsjLrx8cnSBe2XMQ'
user_agent='dc_bot8'

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

