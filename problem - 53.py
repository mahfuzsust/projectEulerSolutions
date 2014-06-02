import math
one_million = 1000000
def getCombinations(n,r):
    return math.factorial(n) / ( math.factorial(r) * math.factorial(n - r) )

count = 0

for i in reversed(xrange(1,101)):
    for j in reversed(xrange(1,i)):
        x = getCombinations(i,j)
        if x > one_million:
            count = count + 1
print count
