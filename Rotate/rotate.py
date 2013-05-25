import argparse,re,itertools

def gen_dictionary(N,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=N:
        t = f.readline()
        t = t.split("\n")[0].split(" ")
        temp = []
        n = int(t[0])
        k = int(t[1])
        temp.append(n)
        temp.append(k)
        j = 0
        g= []
        while j<n:
            y = []
            h = f.readline()
            h = h.split("\n")[0]
            for x in h:
                y.append(x)
            j = j + 1
            g.append(y)
        temp.append(g)
        i = i + 1
        #print temp
        temp_list.append(temp)
    f.close()
    return temp_list

def apply_gravity(m,n):
    i = 0
    x = []
    while i<n:
        t = [row[i] for row in m]
        x.append(t[::-1])
        i = i + 1
    i = 0
    while i<n-1:
        j = 0
        while j<n:
            if x[i][j]!='.' and x[i+1][j]=='.':
                t = x[i][j]
                x[i][j]=x[i+1][j]
                x[i+1][j]=t
                i = 0
                j = -1
            j = j + 1
        i = i + 1 
    return x

def check_pos(l,c,k):
    flag = False
    s = c*k
    for x in l:
        b = ""
        for e in x:
            b = b + e
        if s in b:
            flag = True
            return flag
    i = 0
    while i<len(l):
        j = 0
        b = ""
        while j<len(l):
            b = b + l[j][i]
            j = j + 1
        if s in b:
            flag = True
            return flag
        i = i + 1
    i = k
    while i<n:
        j = 0
        b = ''
        while j<len(l):
            b = b + l[][]



    return flag


def gen_cases(l):
    n = l[0]
    k = l[1]
    m = l[2]
    mg = apply_gravity(m,n)
    for i in m:
        print i
    print "\n"
    for i in mg:
        print i 
    print "\n"
    r = check_pos(mg,'R',k)
    b = check_pos(mg,'B',k)
    if b and r:
        return "Both"
    elif not b and r:
        return "Red"
    elif b and not r:
        return "Blue"
    else:
        return "Neither"

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
for sent in dictionary:
    val = gen_cases(sent)
    #t="Case #"+str(i)+": "+val
    i = i + 1
    #f.write(t)
f.close()