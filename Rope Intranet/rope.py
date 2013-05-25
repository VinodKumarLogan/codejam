import argparse,math

def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    j = 0
    while j<D:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")
        t = temp[0]
        temp_list.append(int(t))
        n = int(t)
        i = 0
        temp = []
        while i<n:
            t = f.readline()
            t1 = t.split("\n")
            t = t1[0].split(" ")
            r = []
            for x in t:
                r.append(int(x))
            temp.append(r)
            i = i + 1
        temp_list.append(temp)
        list_dic.append(temp_list)
        j = j + 1
    #print list_dic
    f.close()
    return list_dic 

def find_value(l):
    n = l[0]
    points = l[1]
    points.sort(key=lambda x: float(x[0]))
    count = 0
    i = 0
    j = 0
    while i<len(points):
        j = i + 1
        while j<len(points):
            x = points[i]
            y = points[j]
            if x[0]<y[0] and x[1]>y[1]:
                count = count + 1
            j = j + 1
        i = i + 1
    return count

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
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()
