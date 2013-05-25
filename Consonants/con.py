import argparse

def gen_dictionary(n,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=n:
        t = [x for x in f.readline().split("\n")[0].split(" ")]
        temp = [t[0],int(t[1])]
        temp_list.append(temp)
        i+=1
    f.close()
    return temp_list

def substr(string,n):
    j=n
    a=list()
    while True:
        for i in range(len(string)-j+1):
            a.append(string[i:i+j])
        if j==len(string):
            break
        j+=1
    return a

def gen_cases(l,vowels=['a','e','i','o','u']):
    n = l[1]
    count = 0
    sub = substr(l[0],n)
    for s in sub:
        i = 0
        while i<len(s):
            j = i
            temp = 0
            while j<(i+n) and j<len(s):
                if s[j] not in vowels:
                    temp+=1
                j+=1
            if temp==n:
                count+=1
                break
            i+=1
    return count


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
    val = gen_cases(l=case)
    t="Case #"+str(i)+": "+str(val)+"\n"
    i = i + 1
    f.write(t)
f.close()