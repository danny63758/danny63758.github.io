import random

patterns_1=['Trump must be impeached now!!!. Joe Biden is the best choice',
'Donald Trump is a criminal and a tyrant. Remove him now and replace him with Joe',
'Joe for 2020! Kick Trump out now and bring in Joe!'
]

pattern_1='Trump must be impeached now!!!. Joe Biden is the best choice'

#result=pattern_1.replace(pattern_1,patterns_1[0])

for i in range(10):

    pattern_1=random.choice(patterns_1)

    result1=pattern_1.replace(pattern_1,patterns_1[0])
    result1=result1.replace(pattern_1,patterns_1[0])

    result1=pattern_1.replace(pattern_1,random.choice(patterns_1))
    result1=result1.replace(pattern_1,random.choice(patterns_1))

    print('result1=',result1)


comment_2.append(result1)