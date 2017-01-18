primes = []

def primecheck(x):
    n = []
    checker = []
    for y in range (2, x+1): 
        z = x/(float(y))
        checker.append(z)
        #print checker
        #print z


    for k in range (0, x-1):
        p = checker[k]
        if p.is_integer() == True:
            n.append(1)
        else:
            s=0

        if sum(n) > 1:
            return 0

    if sum(n) == 1:
        return x

u=input("Type the highest number you want to check for primes: ")
l=input("Type the lowest number you want to check for primes: ")
for x in range (l, u):
    primes.append(primecheck(x))
    primes = [m for m in primes if m != 0]

    print primes

print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print "Prime number(s) between the entered numbers: "
print primes
print ""
print "Total number of primes:"
print len(primes)
