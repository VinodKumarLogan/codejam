import argparse
from math import asin,pi

def compute(filename):
    f = open(filename,'r')
    n = int(f.readline()[:-1])
    for i in range(n):
        temp = f.readline()[:-1].split(" ")
        print "Case #"+str(i+1)+": %.7f" % captainHammer(temp)
    f.close()

def captainHammer(s):
    v = float(s[0])
    d = float(s[1])
    ang = (d*9.8)/(v*v)
    if int(ang)==1:
        return 45.0000000
    else:
        return ((asin(ang))/2.0)*(180.0/pi)

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()
filename = args.filename
compute(filename)