import argparse,math
from decimal import Decimal


def gen_dictionary(D,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for i in f:
    	count = count + 1
    	if count!=1 and count<=(D+1):
            temp_list.append(i.split('\n')[0])
    f.close()
    return temp_list 

def find_value(base,exp):
    result = 1
    while exp:
        if exp & 1:
            result = result * base
        exp = exp >> 1
        base = base *base
    return result


parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
values = f.readline().split(" ")
f.close()
N = int(values[0].split('\n')[0])
global dictionary
dictionary = []
dictionary = gen_dictionary(N,filename)
#print dictionary
global val
val = 3 + math.sqrt(5)
i = 0
f = open("output.txt",'w')
odt = ""
for case in dictionary:
    i=i+1
    outdata=find_value(val,int(case))
    temp = int(outdata)%1000
    #print temp
    if temp<100:
        if temp<10:
            if temp<1:
                odt = "000"
            else:
                odt = "00"+str(temp)
        else:
            odt = "0"+str(temp)
    else:    
        odt = str(temp)
    t = "Case #"+str(i)+": "+odt+"\n"
    f.write(t)
f.close()