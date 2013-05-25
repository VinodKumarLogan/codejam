import argparse

def gen_dictionary(N,filename):
    f = open(filename,'r')
    temp_list = []
    i = 1 
    t = f.readline()
    while i<=N:
        temp = []
        t = [x for x in f.readline().split("\n")[0]]
        temp.extend([t])
        t = [x for x in f.readline().split("\n")[0]]
        temp.extend([t])
        t = [x for x in f.readline().split("\n")[0]]
        temp.extend([t])
        t = [x for x in f.readline().split("\n")[0]]
        temp.extend([t])
        temp_list.append(temp)
        t = f.readline()
        i+=1
    f.close()
    return temp_list


def gen_cases(case):
    rows = case
    cols = []
    diag = [[],[]]
    dc = 0
    for x in zip(*rows):
        t = []
        for y in x:
            t.append(y)
        cols.extend([t])
    diag[0].extend([rows[0][0],rows[1][1],rows[2][2],rows[3][3]])
    diag[1].extend([rows[3][0],rows[2][1],rows[1][2],rows[0][3]])
    for v in rows:
        dc+=v.count('.')
        if v.count('X')+v.count('T')==4:
            return "X won"
        elif v.count('O')+v.count('T')==4:
            return "O won"
    for v in cols:
        if v.count('X')+v.count('T')==4:
            return "X won"
        elif v.count('O')+v.count('T')==4:
            return "O won"
    for v in diag:
        if v.count('X')+v.count('T')==4:
            return "X won"
        elif v.count('O')+v.count('T')==4:
            return "O won"
    if dc>=1:
        return "Game has not completed"
    else:
        return "Draw"

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
dictionary = []
dictionary = gen_dictionary(N,filename)
f = open("output.txt",'w')
i = 1
for case in dictionary:
    val = gen_cases(case)
    t="Case #"+str(i)+": "+val+"\n"
    i = i + 1
    f.write(t)
f.close()