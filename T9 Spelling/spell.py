import argparse,re,itertools


def retrieve_txtmsg(D,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for i in f:
    	count = count + 1
    	if count!=1 and count<=(D+1):
            temp_list.append(i.split('\n')[0])
    f.close()
    return temp_list 

def gen_dictionary():
    temp_list = [[' '],[]]
    temp_list.append(['a','b','c'])
    temp_list.append(['d','e','f'])
    temp_list.append(['g','h','i'])
    temp_list.append(['j','k','l'])
    temp_list.append(['m','n','o'])
    temp_list.append(['p','q','r','s'])
    temp_list.append(['t','u','v'])
    temp_list.append(['w','x','y','z'])
    return temp_list

def type_data(msg):
    i = 0
    val = ""
    prev = 1
    while i<len(msg):
        flag = False
        c = msg[i]
        if c==dictionary[0][0]:
            if prev==0:
                val = val + " "
            val = val + str(0)
            prev = 0
            i = i + 1
            continue
        j = 2
        while j<=9:
            if c in dictionary[j]:
                k = 0 
                while k<len(dictionary[j]): 
                    if c==dictionary[j][k]:
                        if prev==j:
                            val = val + " "
                        prev = j
                        val = val + str(j)*(k+1)
                        flag = True
                        break
                    k = k + 1
                if flag:
                    break
            j = j + 1
        i = i + 1
    return val     
 

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
values = f.readline().split(" ")
f.close()
N = int(values[0].split('\n')[0])
global dictionary
dictionary = []
dictionary = gen_dictionary()
txtmsg = retrieve_txtmsg(N,filename)
i = 0
f = open("output.txt",'w')
for case in txtmsg:
    i=i+1
    outdata=type_data(case)
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()