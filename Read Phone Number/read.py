import sys
def compute(filename):
    f = open(filename,'r')
    n = int(f.readline()[:-1])
    for i in range(n):
        temp = f.readline()[:-1].split(" ")
        print "Case #"+str(i+1)+":",readPhoneNumber(temp).strip()
    f.close()

def readPhoneNumber(s):
    num = s[0]
    ds = s[1].split("-")
    p = 0
    st = ""
    for sp in ds:
        n = num[p:p+int(sp)]
        st+=spellNumber(n)
        p += int(sp)
    return st

def spellNumber(number):
    temp = ""
    i = 0
    global numval
    global countval
    while i<len(number):
        prefix = 1
        value = number[i]
        j = i + 1
        while j<len(number):
            if value==number[j]:
                j+=1
                prefix+=1
            else:
                break
        if prefix==1:
            temp+=numval[value]+" "
        elif prefix>1 and prefix<=10:
            temp+=countval[str(prefix)]+" "+numval[value]+" "
        else:
            temp+=(numval[value]+" ")*prefix
        i = j
    return temp

numval = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
countval = {"2":"double","3":"triple","4":"quadruple","5":"quintuple","6":"sextuple","7":"septuple","8":"octuple","9":"nonuple","10":"decuple"}
compute(sys.argv[1])