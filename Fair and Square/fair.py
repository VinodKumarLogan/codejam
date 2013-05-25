import argparse

def checkPalin(n):
    n = str(n)
    if n==n[::-1]:
        return True
    else:
        return False

def gen_dictionary(n,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=n:
        t = [int(x) for x in f.readline().split("\n")[0].split(" ")]
        temp_list.append(t)
        i+=1
    f.close()
    return temp_list

def gen_cases(case,l):
    a = case[0]
    b = case[1]
    count = 0
    for x in l:
        if x>=a and x<=b:
            count+=1
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

x = 1
x2 = 1
l = []
while x<=(10**8):
    x2 = x*x
    if checkPalin(x) and checkPalin(x2):
        l.append(x2)
    x+=1

dictionary = []
dictionary = gen_dictionary(N,filename)
f = open("output.txt",'w')
i = 1
for case in dictionary:
    val = gen_cases(case,l)
    t="Case #"+str(i)+": "+str(val)+"\n"
    i = i + 1
    f.write(t)
f.close()