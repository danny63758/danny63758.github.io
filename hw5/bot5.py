import praw

username='danny63758'
password='HMBteam4win$'
client_id='zcYXSKffzE32Kg'
client_secret='2Y3xQL4RypcODqJSAaIzVORai0M'
user_agent='dc_bot5'

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

