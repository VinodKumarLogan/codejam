import argparse,math

def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")
        t = temp[0]
        temp_list.append(int(t))
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        temp = []
        for x in t:
            temp.append(int(x))
        temp_list.append(temp)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic 

def find_value(l):
    cost = l[0]
    prices = l[1]
    curMin=max(prices)
    curMaxDiff=0
    sp = 0
    i = 0
    lmin = []
    lmax = []
    while i<len(prices):
    	ele = prices[i]
        if ele < curMin and curMin<=cost:
            curMin=ele
            #print i
            lmin.append(i)
            cp = cost/float(curMin)
        elif (ele-curMin)>curMaxDiff:
            curMaxDiff=ele-curMin
            #print i
            lmax.append(i)
            sp = float(curMaxDiff)*cp
        i = i + 1
    t = ""
    #print lmin
    #print lmax
    if sp!=0:
    	i = 0 
        k = 0
        m = min(lmin)
        #print m
        while i<len(lmin):
    	    if (i+m) == lmin[i]:
    		    k = k + 1
    	    else:
    		    break
       	    i = i + 1
        i = 0 
        j = 0
        m = min(lmax)
        #print m
        while i<len(lmax):
    	    if (i+m) == lmax[i]:
    		    j = j + 1 
    	    else:
    		    break
       	    i = i + 1
    	t = str(k)+" "+str(j+m)+" "+str(int(sp))
    else:
    	t = "IMPOSSIBLE"
    return t

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
f = open("output.txt",'w')
i = 0
for case in dictionary:
    i=i+1
    #print case
    outdata=find_value(case)
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()
