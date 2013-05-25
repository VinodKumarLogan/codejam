import argparse
from math import*

def gen_dictionary(N,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=N:
        t = [int(x) for x in f.readline().split(" ")]
        temp_list.append(t)
        i+=1
    f.close()
    return temp_list

def gen_cases(l):
    r = l[0]
    t = l[1]
    a = 2.0
    b = ((2.0*r)+1.0) - 2.0
    c = (-1.0)*t
    root = (b*b)-(4*a*c)
    val = (-b+sqrt(root))/(2*a)
    t2 = (2*int(val)*int(val)) + int(val)*(b)
    print t2-t
    '''
    val2 = val + 1 
    t2 = (2*val2*val2) + val2*(b)
    val3 = val - 1
    t3 = (2*val3*val3) + val3*(b)
    print val," ",val2," ",val3
    if floor(val)==val:
        return int(val)-1
    else:'''
    if t2-t>0:
        return int(val)-1
    else:
        return int(val)

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
value = f.readline()
f.close()
N = int(value.split('\n')[0])
global dictionary
global sentence
dictionary = []
dictionary = gen_dictionary(N,filename)
f = open("output.txt",'w')
i = 1
for case in dictionary:
    val = gen_cases(case)
    t="Case #"+str(i)+": "+str(val)+"\n"
    i = i + 1
    f.write(t)
f.close()