import sys
def compute(filename):
    f = open(filename,'r')
    n = int(f.readline()[:-1])
    for i in range(n):

        temp = [int(f.readline()[:-1]),[int(x) for x in f.readline()[:-1].split(" ")]]
        print "Case #"+str(i+1)+":",sorting(temp).strip()
    f.close()

def sorting(s):
    alexWorth = list()
    bobWorth = list()
    alexPos = list()
    bobPos = list()
    i = 0
    for x in s[1]:
        if x&1:
            alexWorth.append(x)
            alexPos.append(i)
        else:
            bobWorth.append(x)
            bobPos.append(i)
        i+=1
    alexWorth = sorted(alexWorth)
    bobWorth = sorted(bobWorth,reverse=True)
    result = ['']*s[0]
    i = 0
    for b in bobPos:
        result[b] = str(bobWorth[i])
        i+=1
    i = 0
    for a in alexPos:
        result[a] = str(alexWorth[i])
        i+=1
    return ' '.join(result)

compute(sys.argv[1])