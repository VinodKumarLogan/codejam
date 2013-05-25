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

def num_base(num,base):
    temp = ""
    while num!=0:
        temp = temp + str(num%base)
        num = num/base
    return int(temp[::-1])

def find_min(l):
    i = 2
    flag = False
    while not flag:
        temp = [num_base(i,x) for x in l]
        print temp
        f = False
        for x in temp:
            f = check_happy(x)
            if not f:
                break
        flag = f
        i = i + 1
    return i-1

def check_happy(num):
    t = sum([int(x)**2 for x in str(num)])
    if t==1:
        return True
    elif t>1 and t<9:
        return False
    else:
        return check_happy(t)

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
    outdata=find_min(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()