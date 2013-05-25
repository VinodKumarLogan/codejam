import argparse,re,itertools


def gen_dictionary(N,filename):
    f = open(filename,'r')
    temp_list = []
    i = 0
    t = f.readline()
    while i<N:
        temp = []
        n = int(f.readline().split("\n")[0])
        temp.append(n)
        j = 0
        q = []
        while j<n:
            t = f.readline().split("\n")[0]
            q.append(t)
            j = j + 1
        i = i + 1
        temp.append(q)
        temp_list.append(temp)
    return temp_list 

def find_reverse(sentence):
    q = []
    print sentence
    for s in sentence:
        flag = True
        i = 1
        w = ''
        while flag:
            l = list(itertools.combinations(s,i))
            temp = []
            g = ''
            w = ''
            j = 0
            while j<len(l):
                g = ''
                for e in l[j]:
                    g = g + e
                j = j + 1
                temp.append(g)
            f = True
            for t in temp:
                for u in sentence:
                    if t in u:
                        f = False
                        break
                    else:
                        w = t
                if not f:
                    break
            if not f:
                i = i + 1
            else:
                flag = False
        if w:
            q.append('"'+w+'"')
        else:
            q.append(":(")
    print q
    return q

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
i = 0
f = open("output.txt",'w')
for case in dictionary:
    i=i+1
    #print case
    outdata=find_reverse(case[1])
    #t = "Case #"+str(i)+": "+outdata+"\n"
    #f.write(t)
f.close()