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
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        j = 0 
        temp = []
        while j<temp_list[0]:
            temp.append(float(t[j]))
            j = j + 1   
        temp_list.append(temp)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic 

def find_comb(pos):
    credit = pos[0]
    n = pos[1]
    items = pos[2]
    i = 0
    while i<n:
        j = i + 1
        while j<n:
            if (items[i] + items[j])==credit:
                if j>i:
                    comb = str(i+1)+" "+str(j+1)
                else:
                    comb = str(j+1)+" "+str(i+1)
                break
            j = j + 1
        i = i + 1
    return comb

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
    #outdata=find_comb(dictionary[i])
    i = i + 1
    #t = "Case #"+str(i)+": "+outdata+"\n"
    #f.write(t)
f.close()