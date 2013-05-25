import argparse

def gen_dictionary(N,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=N:
        temp = []
        t = [int(x) for x in f.readline().split(" ")]
        temp.extend(t)
        t = [int(x) for x in f.readline().split(" ")]
        temp.append(t)
        #print temp
        temp_list.append(temp)
        i+=1
    f.close()
    return temp_list

def gen_cases(l):
    e = l[0]
    r = l[1]
    ac = l[3]
    gain = 0
    if r==e:
        gain = sum([x*e for x in ac])
    elif r>e:
        gain+=ac[0]*e
        r = e
        for a in ac[1:]:
            gain+=a*e
    else:
        for a in sorted(ac,reverse=True):
            gain+=e*a
            e = r
    return gain


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