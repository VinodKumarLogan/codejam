import argparse

def gen_dictionary(n,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=n:
        temp = []
        t = [int(x) for x in f.readline().split("\n")[0].split(" ")]
        temp.extend(t)
        t = [int(x) for x in f.readline().split("\n")[0].split(" ")]
        temp.extend([t])
        j = 0
        while j<temp[1]:
            t = []
            r = [int(x) for x in f.readline().split("\n")[0].split(" ")]
            t.extend(r)
            temp.append(t)
            j+=1
        temp_list.append(temp)
        i+=1
    f.close()
    return temp_list

def gen_cases(l):
    keylist = l[2]
    n = l[1]
    temp = []
    keysNeeded = {}
    i = 0
    for x in l[3:]:
        i+=1
        keysNeeded[i] = x[0]
    contents = {}
    i = 0
    for x in l[3:]:
        i+=1
        try:
            contents[i] = x[2:]
        except:
            contents[i] = []
    print l
    print keysNeeded
    print contents
    retlist = []
    unlockable = []
    while len(retlist)!=n:
        for k in keylist:
            for key,value in keysNeeded.items():
                if value==k:
                    unlockable.extend(key)
        unlockable.sort()
        ch = unlockable[0]
        unlockable = unlockable[1:]
        retlist.extend(ch)
        keylist.extend(contents[ch])
        del keylist[ch]

    return '0'

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
value = f.readline()
f.close()
N = int(value.split('\n')[0])
global dictionary
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