import argparse,re,itertools


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

def find_ruler(s):
    r = s[-1:]
    if r in'yY':
        temp = "nobody"
    elif r in 'aeiouAEIOU':
        temp = "a queen"
    else:
        temp = "a king"
    return temp

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
i = 0
f = open("output.txt",'w')
for case in dictionary:
    i=i+1
    outdata=find_ruler(case)
    t = "Case #"+str(i)+": "+case+" is ruled by "+outdata+".\n"
    f.write(t)
f.close()