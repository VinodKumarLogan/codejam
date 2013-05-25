import argparse,re,itertools


def gen_dictionary(N,filename):
    f = open(filename,'r')
    temp_list = []
    i = 0
    t = f.readline()
    while i<N:
        temp = f.readline().split('\n')[0]
        temp_list.append(temp)
        i = i + 1
    return temp_list 

def find_spell(sentence):
	flag = False
    while flag:
        i = 1
        if len(sentence)>(2*i):
            start = sentence[:i]
            end  = sentence[-i:]
            if start==end:
                

	return temp

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
dictionary = gen_dictionary(N,filename)
#print dictionary
i = 0
f = open("output.txt",'w')
for case in dictionary:
    i=i+1
    print case
    #utdata=find_reverse(case)
    #t = "Case #"+str(i)+": "+outdata+"\n"
    #f.write(t)
f.close()