import numpy

def primesfrom2to(n):
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype = numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[       k * k / 3     ::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

a = list(primesfrom2to(1000000))
xxx = 0
ppp = 0
for i in a:
    glag = False
    gr = 0
    for j in range(0,a.index(i)):
        summ = 0
        count = 0
        
        flag = False
        for k in range(j,a.index(i)):
            summ = summ + a[k]
            if summ == i:
                flag = True
                break;
            if summ > i:
                break;
            count = count + 1
        if flag == True:
            glag = True
            if count > gr:
                gr = count
    if glag == True:
        
        if xxx < gr:
            xxx = gr
            ppp = i
            print "mahfuz"
            print i
            print gr

print ppp
print xxx
