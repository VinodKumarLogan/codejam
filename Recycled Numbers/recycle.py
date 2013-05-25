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
        t = temp[0].split(" ")
        temp_list.append(int(t[0]))
        temp_list.append(int(t[1]))
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic 

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
    print dictionary[i]
    #outdata=find_poss(dictionary[i])
    i = i + 1
    #t = "Case #"+str(i)+": "+str(outdata)+"\n"
    #f.write(t)
f.close()