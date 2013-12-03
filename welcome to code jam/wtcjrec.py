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

def num_subsequences(seq, sub):
    if not sub:
        return 1
    elif not seq:
        return 0
    result = num_subsequences(seq[1:], sub)
    if seq[0] == sub[0]:
        result += num_subsequences(seq[1:], sub[1:])
    return result


parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()

filename = args.filename

f = open(filename,'r')
value = f.readline()
f.close()
N = int(value.split('\n')[0])
global dictionary
dictionary = []
dictionary = gen_dictionary(N,filename)
#print dictionary
f = open("output.txt",'w')
i = 1
for sent in dictionary:
    sentence = "welcome to code jam"
    count = num_subsequences(sent,sentence)
    c = count%10000
    if c<1000:
        if c<100:
            if c<10:
                x="000"+str(c)
            else:
                x="00"+str(c)
        else:
            x="0"+str(c)
    else:
        x=str(c)
    t="Case #"+str(i)+": "+x+"\n"
    f.write(t)
    i = i + 1
f.close()