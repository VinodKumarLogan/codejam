import argparse,re,itertools


def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")
        t = temp[0].split(" ")
        temp_list.append(int(t[0]))
        temp_list.append(int(t[1]))
        temp_list.append(int(t[2]))
        j = 0 
        temp = []
        while j<temp_list[0]:
            temp.append(int(t[j+3]))
            j = j + 1   
        temp=sorted(temp)
        temp_list.append(temp)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic 

def check_values(l,p):
    flag = False
    for i in l:
        if i>=p:
            flag = True
            break
    return flag

def find_comb(score,p):
    temp = []
    v1 = v2 = v3 = 0
    if score%3 == 0:
        v1 = v2 = v3 = (score/3)
    elif score%3 == 1:
        v2 = v3 = (score/3)
        v1 = v2 + 1
    else:
        v3 = (score/3)
        v1 = v2 = v3 + 1
    l = [v1,v2,v3]
    if check_values(l,p):
        temp.append(1)
    else:
        temp.append(0)    
    if v1>v2 and v2==v3 and v3!=0:
        l=[v1,v2+1,v3-1]
    elif v1==v2 and v2==v3 and v1!=10 and v3!=0:
        l=[v1+1,v2,v3-1]
    elif v1!=10 and v2!=0:
        l=[v1+1,v2-1,v3]
    else:
        l=[]
    if check_values(l,p):
        temp.append(1)
    else:
        temp.append(0)    
    return temp

def val_sort(l):
    i = 0 
    c00 = 0
    while i<len(l):
        if l[i][0]==0 and l[i][1]==0:
            c00 = c00 + 1
        else:
            break
        i = i + 1
    c01 = c00
    while i<len(l):
        if l[i][0]==0 and l[i][1]==1:
            c01 = c01 + 1
        else:
            break
        i = i + 1
    c11 = c01
    while i<len(l):
        if l[i][0]==1 and l[i][0]==1:
            c11 = c11 + 1
        else:
            break
        i = i + 1
    c10 = c11
    while i<len(l):
        if l[i][0]==1 and l[i][0]==1:
            c11 = c11 + 1
        else:
            break
        i = i + 1
    templ=[]
    if l[c00:c01]:
        for x in l[c00:c01]:
            templ.append(x)
    if l[c11:c10]:
        for x in l[c11:c10]:
            templ.append(x)
    if l[c01:c11]:
        for x in l[c01:c11]:
            templ.append(x)
    if l[:c00]:
        for x in l[:c00]:
            templ.append(x)
    return templ

def calc_pos(l,n,s):
    i = j = k = tsum = 0
    l = val_sort(l)
    #print l
    while i<len(l):
        #print i
        if l[i][0]==0 and l[i][1]==1:
            if j<s:
                tsum = tsum + 1
                j = j + 1
            else:
                k = k + 1
        elif l[i][0]==1 and l[i][1]==0:
            if k<n-s:
                tsum = tsum + 1
                k = k + 1
            else:
                j = j + 1
        elif l[i][0]==0 and l[i][1]==0:
            if k<n-s:
                k = k + 1
            else:
                j = j + 1
        else:
            tsum = tsum + 1
            if j<s:
                j = j + 1
            else:
                k = k + 1
        i = i + 1
    return tsum

def find_poss(pos):
    n = pos[0]
    s = pos[1]
    p = pos[2]
    scores = pos[3]
    l = []
    pos = 0
    for i in scores:
        l.append(find_comb(i,p))
    pos = calc_pos(l,n,s)
    #print pos
    return pos

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
    #print dictionary[i]
    outdata=find_poss(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+str(outdata)+"\n"
    f.write(t)
f.close()