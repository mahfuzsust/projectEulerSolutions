import numpy

x = []
x.append('1')
x.append('12')
x.append('123')
x.append('1234')
x.append('12345')
x.append('123456')
x.append('1234567')
x.append('12345678')
x.append('123456789')
x.append('0123456789')

def primesfrom2to(n):
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype = numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[       k * k / 3     ::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

a = primesfrom2to(1003518800)
print a[-1]
print len(a)
print "program begin"
def is_prime(n):
    if n in a:
        return True;
    return False;

def is_pandigital(n):
    s = ''.join(sorted(str(n))) 
    if s in x:
        return True;
    return False;


for i in a:
    if is_pandigital(i):
        print i

print "finish"
