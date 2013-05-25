import argparse,re,itertools


def gen_dictionary(D,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for i in f:
    	count = count + 1
    	if count!=1 and count<=(D+1):
            temp = [x for x in i.split('\n')[0].split(" ")]
            k = 0
            B = []
            O = []
            temp = temp[1:]
            while k<len(temp):
                if temp[k]=='B':
                    B.append(int(temp[k+1]))
                else:
                    O.append(int(temp[k+1]))
                k+=2
            temp_list.append([B,O])
    f.close()
    return temp_list 

def min_count(l):
    B = l[0]
    O = l[1]
    i = j = mv = 0
    b = o = 1
    while i<len(B) or j<len(O):
        if i!=len(B):
            mv += 1
            if B[i]==b:
                i += 1
                continue
            elif B[i]>b:
                b+=1
            else:
                b-=1
        if j!=len(O):
            mv += 1
            if O[j]==o:
                j += 1
                continue
            elif O[j]>o:
                o+=1
            else:
                o-=1
    return mv

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
    i+=1
    outdata=min_count(case)
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()