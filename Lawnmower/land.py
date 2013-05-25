import argparse

def gen_dictionary(n,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=n:
        t = [int(x) for x in f.readline().split("\n")[0].split(" ")]
        N = t[0]
        M = t[1]
        temp = [N,M,[]]
        j = 0
        while j<N:
            t = [int(x) for x in f.readline().split("\n")[0].split(" ")]
            temp[2].extend([t])
            j+=1
        temp_list.append(temp)
        i+=1
    f.close()
    return temp_list


def checkArray(n,ar):
    for x in ar:
        if x>n:
            return False
    return True

def gen_cases(case):
    n = case[0]
    m = case[1]
    arh = case[2]
    arv = []
    for x in zip(*arh):
        t = []
        for y in x:
            t.append(y)
        arv.extend([t])
    i = 0
    #print arh
    #print arv
    while i<n:
        j = 0
        while j<m:
            if (not checkArray(arh[i][j],arv[j])) and (not checkArray(arh[i][j],arh[i])):
                return "NO" 
            j+=1
        i+=1
    return "YES"


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
    t="Case #"+str(i)+": "+val+"\n"
    i = i + 1
    f.write(t)
f.close()