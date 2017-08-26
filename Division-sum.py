import sys
c=0
def divisibleSumPairs(n, k, ar):
    global c
    print n
    print k

    # Complete this function
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            s=ar[j]+ar[j]
            if(s%k==0):
                c=c+1
                print "divisible pair",ar[i],ar[j]

        

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
print ar
divisibleSumPairs(n, k, ar)
