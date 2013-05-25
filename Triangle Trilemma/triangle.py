import argparse,math


def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        temp = []
        for x in t:
            temp.append(int(x))
        list_dic.append(temp)
        i = i + 1
        #print temp
    f.close()
    return list_dic 

def check_type(l):
    t = []
    t.append((l[0][0]-l[1][0])**2 + (l[0][1]-l[1][1])**2)
    t.append((l[2][0]-l[1][0])**2 + (l[2][1]-l[1][1])**2)
    t.append((l[0][0]-l[2][0])**2 + (l[0][1]-l[2][1])**2)
    t = sorted(t)   
    m = t[2]
    ttype1 = "" 
    if t[1] + t[0] == m:
        ttype1 = "right"
    elif t[1] + t[0] > m:
        ttype1 = "acute"
    else:
        ttype1 = "obtuse"
    l1=math.sqrt(t[0])
    l2=math.sqrt(t[1])
    l3=math.sqrt(t[2])
    ttype2 = ""
    if l1==l2 or l2==l3 or l3==l1:
        ttype2 = "isosceles"
    else:
        ttype2 = "scalene"
    return ttype2+" "+ttype1+" triangle"

def check_triangle(l):
    det = l[0][0]*(l[1][1]*l[2][2] - l[1][2]*l[2][1]) - l[0][1]*(l[1][0]*l[2][2] - l[2][0]*l[1][2]) + l[0][2]*(l[1][0]*l[2][1] - l[2][0]*l[1][1])
    if det==0:
        return False
    else:
        return True

def find_comb(coord):
    i = 0
    l = []
    flag = True
    #print coord,"\n"
    while i<len(coord):
        l.append([coord[i],coord[i+1],1])
        i = i + 2
    if not check_triangle(l):
        return "not a triangle"
    else:
        t_type = check_type(l)
        return t_type
    



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
    outdata = find_comb(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()