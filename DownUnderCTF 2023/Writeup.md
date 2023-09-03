The code we started with is as follows:

"""
message = open('./message.txt', 'rb').read() + open('./flag.txt', 'rb').read()

palette = '.=w-o^*'
template = list(open('./mask.txt', 'r').read())

canvas = ''
for c in message:
    for m in [2, 3, 5, 7]:
        while True:
            t = template.pop(0)
            if t == 'X':
                canvas += palette[c % m]
                break
            else:
                canvas += t

print(canvas)
"""

A non-trivial amount of this code is simply used to map the message and flag to the logo of the competition. Removing it leaves us with this. 

