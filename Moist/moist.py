import argparse,re,itertools

def compute(filename):
    f = open(filename,'r')
    n = int(f.readline()[:-1])
    for i in range(n):
        temp = [int(f.readline()[:-1])]
        temp_ar = list()
        for j in range(temp[0]):
            temp_ar.append(f.readline()[:-1])
        temp.append(temp_ar)
        print "Case #"+str(i+1)+": "+str(moist(temp))
    f.close()

def moist(s):
    n = s[0]
    ds = s[1]
    count = 0
    k = ds[0]
    for j in range(1,n):
        t = ds[j]
        if k>t:
            count+=1
        else:
            k=t
    return count

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()
filename = args.filename
compute(filename)