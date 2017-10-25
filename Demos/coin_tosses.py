import random

def cointosses():
    # flip a coin 5,000 times
    heads = 0
    tails = 0
    for toss in range(10):
        # how to determine head or tail
        # let's make a head 0 and a tail 1
        result = random.randint(0,1)
        # if we get a head or a 0, increment the head count
        if (result == 0):
            heads += 1
            output = "head"
        # if we get a tail, increment the tail count
        else:
            tails += 1
            output = "tail"
        
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(toss+1, output, heads, tails)

cointosses()