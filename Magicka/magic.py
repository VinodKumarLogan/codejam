import argparse,re,itertools

def gen_dictionary(D,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for x in f:
    	count = count + 1
    	if count!=1 and count<=(D+1):
            tlst = []
            t = x.split('\n')[0]
            t = x.split(" ") 
            m = int(t[0])
            i = 0
            temp = []
            while i<m:
                temp.append(t[i+1])
                i = i + 1
            tlst.append(temp)
            i = m + 1
            r = int(t[i])
            k = 0
            temp = []
            while k<r:
                temp.append(t[i+k+1])
                k = k + 1
            tlst.append(temp)
            temp = []
            temp.append(t[-2:-1])
            temp.append(t[-1:][0].split("\n")[0])
            #print temp
            tlst.append(temp)
            temp_list.append(tlst)
    f.close()
    return temp_list

def modify_rep(s,l):
    c1 = s[-1:]
    c2 = s[-2:-1]
    t = s
    i = 0
    while i<len(l):
        x = l[i]
        c1 = t[-1:]
        c2 = t[-2:-1] 
        if (c1==x[0] and c2==x[1]) or (c1==x[1] and c2==x[0]):
            t = t[0:-2] + x[2]
        else:
            i = i + 1
        #print i
    return t

def modify_rem(s,l):
    i = 0
    t = s
    while i<len(l) and len(s)>1:
        x = l[i] 
        if len(t)>1 and (x[0] in t) and (x[1] in t):
            t=""
        i = i + 1
    return t

def gen_cases(l):
    temp = ""
    for x in l[2][1]:
        temp = temp + x
        #print temp
        if len(temp)>1:
            temp = modify_rep(temp,l[0])
            temp = modify_rem(temp,l[1])
    t = []
    for x in temp:
        t.append(x)
    return t


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
sentence = "welcome to code jam"
dictionary = []
dictionary = gen_dictionary(N,filename)
f = open("output.txt",'w')
i = 1
for sent in dictionary:
    count = gen_cases(sent)
    t="Case #"+str(i)+": ["
    for x in count:
        t = t + x + ", "
    if count:
        t = t[:-2]
    t = t + "]\n"
    i = i + 1
    f.write(t)
f.close()