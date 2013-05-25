import argparse,re,itertools


def gen_dictionary(D,filename):
    f = open(filename,'r')
    temp_list = []
    count = 0
    for i in f:
    	count = count + 1
    	if count!=1 and count<=(D+1):
            temp_list.append(i.split('\n')[0])
    f.close()
    return temp_list 

def find_reverse(sentence):
	revsent = sentence.split(" ")
	temp = ""
	for i in revsent:
		temp = i + " " + temp
	#print temp
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
    outdata=find_reverse(case)
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()