import argparse,math
def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        t = f.readline()
        list_dic.append([x for x in t.split("\n")[0].split(" ")])
        i+=1
    f.close()
    return list_dic

def find_num(l):
    code = l[0]
    al1 = l[1]
    al2 = l[2]
    l1 = len(al1)
    l2 = len(al2)
    n1 = [al1.index(x) for x in code]
    i = len(n1)-1
    num = 0
    while i>=0:
        num+=int(pow(l1,i))*n1[len(n1)-i-1]
        i-=1
    temp = num
    n = ''
    while temp!=0:
        n = al2[temp%l2] + n
        temp /= l2
    return n

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
    outdata=find_num(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()