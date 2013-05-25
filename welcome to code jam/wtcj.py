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

def gen_cases(case):
    i = j = count = 0
    #print sentence[0]
    case = case.lower()
    t = 0
    lptr = 0
    while i<len(case):
    	if sentence[0]==case[i]:
    		mptr = i
    		t = t + 1
    		if t==1:
    			f = i
    	i = i + 1
    lptr = mptr
    if t==0:
    	return 0
    mptr = f
    i = 0
    while mptr<=lptr:
        c = sentence[i]
    	if c!=case[j]:
    		j = j + 1
    		if j==len(case):
    			i = i - 1
    			if case[i]==sentence[0]:
    				mptr = i
    			while case[j]!=sentence[i]:
    				j = j - 1
    	else:
    	    i = i + 1
    	    j = j + 1	
    	if i>len(case):
    		count = count + 1

    print mptr
    return 0


parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
value = f.readline()
f.close()
N = int(value.split('\n')[0])
global dictionary
global sentence
sentence = "welcome to code jam"
dictionary = []
dictionary = gen_dictionary(N,filename)
print dictionary
f = open("output.txt",'w')
i = 1
for sent in dictionary:
	#print sent
    count = gen_cases(sent)
    print count
    t="Case #"+str(i)+": "+str(count)+"\n"
    f.write(t)
f.close()