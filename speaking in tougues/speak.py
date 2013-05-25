import argparse,re,itertools


def retrieve_msg(D,filename):
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
    temp_list = {}
    i = 0
    l1=[]
    while i<26:
        l1.append(chr(ord('a')+i))
        i = i + 1
    l2=['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
    i = 0
    while i<26:
        temp_list[l2[i]]=l1[i]  
        i = i + 1   
    return temp_list

def grese_to_eng(msg):
    val = ""
    for i in msg:
        if i!=" ":
            t = dictionary[i]
        else:
            t = " "
        val = val + t 
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
dictionary = {}
dictionary = gen_dictionary()
#print dictionary
txtmsg = retrieve_msg(N,filename)
i = 0
f = open("output.txt",'w')
for case in txtmsg:
    i=i+1
    outdata=grese_to_eng(case)
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()