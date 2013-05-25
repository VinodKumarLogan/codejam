from time import time

def checkPalin(n):
	n = str(n)
	if n==n[::-1]:
		return True
	else:
		return False

def countDig(n):
	c = 0
	t = n - 0 
	while t!=0:
		t/=10
		c+=1
	return c

x = 1
x2 = 1
l = {}
t1 = time()
while x<=(10**8):
	x2 = x*x
	if checkPalin(x) and checkPalin(x2):
		l[x]= x2
	x+=1
print time()-t1
f = {}
print sorted(l.values())[-1:]
for x in l.keys():
	try:
		f[countDig(x)]+=1
	except:
		f[countDig(x)]=1
print f