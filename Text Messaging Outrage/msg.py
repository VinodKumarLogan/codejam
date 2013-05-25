import argparse,re,itertools


def gen_dictionary(N,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<N:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")[0].split(" ")
        t = []
        for x in temp:
            temp_list.append(int(x)) 
        temp = []
        t = f.readline().split("\n")[0].split(" ")
        for x in t:
            temp.append(int(x))
        temp_list.append(temp)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic

def find_count(ld):
    P = ld[0]
    K = ld[1]
    L = ld[2]
    l = ld[3]
    l = sorted(l,reverse=True)
    i = 0
    j = 0
    count = 0 
    while i<L:
        if i%K==0:
            j = j + 1
        count = count + j*l[i]
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
#print dictionary
i = 0
f = open("output.txt",'w')
while i<N:
    #print dictionary[i]
    outdata=find_count(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()