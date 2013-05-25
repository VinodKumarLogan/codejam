import argparse,math


def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        temp = []
        for x in t:
            temp.append(int(x))
        list_dic.append(temp)
        i = i + 1
        #print temp
    f.close()
    return list_dic 

def find_comb(l):
    N = l[0]
    K = l[1]
    chain = [[False,True]]
    i = 0
    bk = K
    bn = (1<<N)-1
    r = bn & bk
    if r==bn:
        return "ON"
    else:
        return "OFF"



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
    outdata = find_comb(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()