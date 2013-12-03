import argparse,re,itertools


def gen_dictionary(D,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for i in f:
    	count = count + 1
    	if count!=1 and count<=(D+1):
            temp_list.append(i.split('\n')[0])
    f.close()
    return temp_list 


def gen_cases(limit,N,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for i in f:
    	count = count + 1
    	if count>limit and count<=(limit+N+1):
            temp_list.append(i.split('\n')[0])
    f.close()
    return temp_list


def find_possibilities(case):
    l1=[]
    i=0
    j=0
    length = []
    while i<len(case):
        l=[]
        count = 0
        if case[i]=="(":
            j=i+1
            while case[j]!=")":
                l.append(case[j])
                j = j + 1
                count = count + 1
            length.append(count)         
            i = j + 1        
        else:
            length.append(1)
            l.append(case[i])
            i = i+1
        l1.append(l)
    words = []
    words = find_words(l1,length)
    return words


def find_words(pos,length):
    n = len(pos)
    l = []
    no_of_pos = 1
    length_of_str = 0
    for i in length:
        no_of_pos = no_of_pos * i
        length_of_str = length_of_str+1
    l=[]
    val = 0
    i=0
    for word in dictionary:
        i = 0
        while i<length_of_str:
            flag = 1
            for temp in word:
                if temp in pos[i]:
                    i = i + 1
                else:
                    flag = 0
                    break
            if flag==1:
                val = val + 1
            else:
                break
    return val



parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
values = f.readline().split(" ")
f.close()
L = int(values[0])
D = int(values[1])
N = int(values[2].split('\n')[0])
global dictionary
dictionary = []
dictionary = gen_dictionary(D,filename)

cases = []
cases = gen_cases(D+1,N,filename)
outdata=[]
i = 0
f = open("output.txt",'w')
for case in cases:
    i=i+1
    outdata=find_possibilities(case)
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()


#print dictionary
#print cases