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
        t = temp[0]
        temp_list.append(int(t))
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        temp = []
        for x in t:
            temp.append(int(x))
        temp_list.append(temp)
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        temp = []
        for x in t:
            temp.append(int(x))
        temp_list.append(temp)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic 

def find_comb(pos):
    n = pos[0]
    l = []
    v1 = sorted(pos[1])
    v2 = sorted(pos[2],reverse=True)
    i = 0
    tsum = 0
    while i<n:
        tsum = tsum + v1[i]*v2[i]
        i = i + 1
    return tsum

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
    outdata=find_comb(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()