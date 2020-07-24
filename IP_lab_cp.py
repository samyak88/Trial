'''class strr_pal:
	l=0
	s_new=""
	def __init__(self,s_org):
		self.s_org=s_org
		self.l=len(s_org)

	def construct_pal(self):
		c=[]
		a=0
		b=0
		for i in range(self.s_org.count("?")):
			c.append(self.s_org.index("?",a))     # index of "?" after a
			a=c[i]+1
		

		for i in self.s_org:
			if i!="?":
				self.s_new+=i
			else:
				if self.s_org[-c[b]-1]!="?":
					self.s_new+=self.s_org[-c[b]-1]
					b+=1
				else:
					self.s_new+="a"
					b+=1

		if self.s_new!=self.s_new[::-1]:
			print(-1)
		else:
			print(self.s_new)

uv=strr_pal("aab?a??aa")
uv.construct_pal()
'''
def min_steps(n, l):
    a=0
    while l.count(l[0])!=n:
        l.sort()
        for i in l[:-1]:
            l.remove(i)
            l.append(i+1)
        a+=1
    return a
print(min_steps(5,[1,2,3,4,5]))



'''
def isPalindrome(n):
	if len(str(n))<=1:
		return True
	elif str(n)[0]==str(n)[1]:
		return f1(str(n)[1:-1])
	else:
		return False 

print(isPalindrome(20021))
'''






'''
class m:
	def __init__(self,k=8):
		self.x=8
		#print(self.x)
	def __str__(self):
		return str(self.x)
def scale(a,b):
		a.x =a.x*b
		print (a.x)

s=m()
t=m(4)
#scale(s,2)
print(s)
#scale(t,2)
print(t)'''
'''
class date:
	def __init__(self,d,m,y):
		self.__date=d
		self.__month=m
		self.__year=y

	def getMonth(self):
		return self.__month

	def setMonth(self,a):
		if 1<=a<=12:
			self.__month =a

z=date(12,4,2019)
#print(z.__month)
z.setMonth(12)
print(z.getMonth())
print(type (z.getMonth()))'''




'''
n=int(input())
weights=[float(i) for i in input().split()]
target=int(input())

def w(t,weightL):
    weightL.sort()
    if t<0:
        return False
    for i in weightL:
        if t==i or t%i==0:
            return (True)
        
    for k in weightL:
        return w(t-k,weightL)

print(w(target,weights))
'''



l="abc"
#l=[2,5,6,3]
subsets=[[]]
for i in l:
    subsets+= [y + [i] for y in subsets]
print(subsets)

a=input()
print(a)
