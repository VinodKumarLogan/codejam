import argparse,re,itertools


def gen_dictionary(N,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<N:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")
        s = int(temp[0].split(" ")[0])
        temp_list.append(s)
        j = 0 
        temp = []
        t = f.readline().split("\n")[0].split(" ")
        for x in t:
            temp.append(int(x))
        temp_list.append(temp)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic

def find_odd(l):
    n = l[0]
    guests = l[1]
    i = 0
    while len(guests)!=1:
        temp = guests[0]
        try:
            lindex = guests[1:].index(temp)
            del guests[lindex+1]
            del guests[0]
        except:
            return temp
    return guests[0]

        

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
    outdata=find_odd(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()