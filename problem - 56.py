def getSum(n):
    n = str(n)
    summ = 0
    for i in n:
        summ = summ + int(i) 
    return summ
gr = 0
for i in reversed(xrange(1,101)):
    for j in reversed(xrange(1,101)):
        x = getSum ( i ** j )
        if x > gr:
            gr = x
print gr
            
