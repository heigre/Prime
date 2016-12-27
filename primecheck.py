n = []
checker = []
x = 400001611
for y in range (2, x+1): 
    z = x/(float(y))
    checker.append(z)
    #print checker
    print z


for k in range (0, x-1):
    p = checker[k]
    if p.is_integer() == True:
        n.append(1)
    else:
        s=0

    if sum(n) > 1:
        print ""
        print ""
        print ""
        print n
        print x
        print "Sadly, it is not a prime"
        break

if sum(n) == 1:
    print ""
    print ""
    print ""
    print n
    print x
    print "It is a prime!"


