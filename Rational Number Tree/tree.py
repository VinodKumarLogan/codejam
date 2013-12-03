import sys
def compute(filename):
    f = open(filename,'r')
    n = int(f.readline()[:-1])
    for i in range(n):
        temp = f.readline()[:-1].split(" ")
        if int(temp[0])&1:
            print "Case #"+str(i+1)+":",bottomTop(int(temp[1]))
        else:
            print "Case #"+str(i+1)+":",topBottom(int(temp[1]),int(temp[2]))
    f.close()

def topBottom(p,q):
    n =1
    while p!=1 and q!=1:
        if p>q:
            
    return n

def bottomTop(n):
    return 0

compute(sys.argv[1])