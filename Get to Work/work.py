import argparse,re,itertools


def gen_dictionary(D,filename):
    f = open(filename,'r')
    list_dic = []
    t = f.readline()
    i = 0
    while i<D:
        temp_list = []
        t = f.readline()
        temp = t.split("\n")[0].split(" ")
        n = int(temp[0])
        t = int(temp[1])
        temp_list.append(n)
        temp_list.append(t)
        e = int(f.readline().split("\n")[0])
        t1 = []
        t1.append(e)
        j = 0 
        t2 = []
        while j<e:
            temp = []
            t = f.readline().split("\n")[0].split(" ")
            temp.append(int(t[0]))
            temp.append(int(t[1]))
            j = j + 1
            t2.append(temp)
        t1.append(t2)
        temp_list.append(t1)
        list_dic.append(temp_list)
        i = i + 1
    f.close()
    return list_dic


def find_route(l):
    n = l[0]
    t = l[1]
    e = l[2][0]
    hp = l[2][1]
    i = 0
    move = [[] for _ in range(n)]
    drive = [False]*n
    while i<e:
        home = hp[i][0]-1
        move[home].extend([hp[i][1]])
        drive[home] = True
        i = i + 1 
    i = 0
    while i<n:
        x = move[i]
        if x:
            x = sorted(x,reverse=True)
            if sum(x)<len(x) and (i+1)!=t:
                return "IMPOSSIBLE"
        i = i + 1
    i = 0
    c = [0]*n
    while i<n:
        if drive[i]:
            j = 1
            while j<=len(move[i]):
                flag = False
                temp = list(itertools.combinations(move[i],j))
                for q in temp:
                    if len(move[i])<=sum(q):
                        c[i] = len(q)
                        flag = True
                        break
                if flag:
                    break
                j = j + 1
        i = i + 1
    count = ""
    for x in c:
        count = count + str(x) + " "
    count = count[:-1]
    return count


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
    outdata=find_route(dictionary[i])
    i = i + 1
    t = "Case #"+str(i)+": "+outdata+"\n"
    f.write(t)
f.close()