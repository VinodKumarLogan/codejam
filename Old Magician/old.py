import argparse


def gen_dictionary(N,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<N:
        t = f.readline().split("\n")[0].split(" ")
        temp_list = [int(x) for x in t]
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic

def find_color(l):
    w = l[0]
    b = l[1]
    if b%2==1:
        return "BLACK"
    else:
        return "WHITE"

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
    outdata=find_color(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()