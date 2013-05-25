import argparse,re,itertools


def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")
        s = int(temp[0].split(" ")[0])
        t1 = []
        t1.append(s)
        j = 0 
        temp = []
        while j<s:
            t = f.readline().split("\n")[0]
            temp.append(t)
            j = j + 1
        t1.append(temp)
        temp_list.append(t1)
        j = 0
        t2 = []
        q = int(f.readline().split("\n")[0])
        t2.append(q)
        temp = []
        while j<q:
            t = f.readline().split("\n")[0]
            temp.append(t)
            j = j + 1
        t2.append(temp)
        temp_list.append(t2)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic

def find_pass(l):
    s = l[0][0]
    q = l[1][0]
    engines = l[0][1]
    queries = l[1][1]
    i = 0
    count = 0
    temp = [[x for x in engines],[False for x in engines]]
    #print temp
    t = temp
    while i<q:
        pos = t[0].index(queries[i])
        #print pos
        t[1][pos]=True
        #print t
        c = 0
        for x in t[1]:
            if x:
                c = c + 1
        if c == s:
            count = count + 1
            t = [[x for x in engines],[False for x in engines]]
            i = i - 1
        i = i + 1
    return count

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
values = f.readline().split("\n")
f.close()
N = int(values[0].split('\n')[0])
global dictionary
dictionary = []
dictionary = gen_dictionary(N,filename)
i = 0
f = open("output.txt",'w')
while i<N:
    #print dictionary[i]
    outdata=find_pass(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()