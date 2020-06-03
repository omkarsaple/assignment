

#DAY 1
'''
2nd question
n=int(input('enter number:'))
l={}
for i in range(1,n+1):
    l[i]=i*i
print(l)

1st question
s=int(input('enter the starting number:'))
e=int(input('enter the ending number:'))
l=[]
for i in range(s,e):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)        

4th que
n=int(input('enter your number:'))
if n%2==0:
    print('number is even')
else:
    print('number is odd')

5th que
a=int(input('enter your age:'))
if a<8 or a>12:
    print('sorry not allowed..byee')
else:
    print('u r welcome')

3rd que
s=input('enter your sentence:')
print(s.upper())
'''
#DAY 2
'''
2nd question=count even AND ODD no
l=[1,2,3,4,5,6,7,8,9]
e=0
o=0
for i in l:
    if i%2==0:
        e+=1
    else:
        o+=1
print('count of even numbers:',e)
print('count of odd numbers:',o)

3rd question=create multiplication table
l=1
n=10
for i in range(1,n+1):
    s=l*i
    print(l,'*',i,'=',s)

5th question=pattern
n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print()    

1st que=series 
n=int(input('enter the number:'))
s=0
for i in range(1,n+1):
    s=s+i
    print(i,end="")
    if i<n:
        print("+",end="")
print('=',s)

4th ques=row wise sum
def row_sum(n):
    n=pow(n,3)
    return n
print(row_sum(2))
print(row_sum(4))
'''
#DAY 3
'''
3rd que=PATTERN
n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()  

5th que=NARCISSTIC NO
n=int(input('enter number:'))
ip=n
s=0
l=len(str(n))
while n!=0:
    r=n%10
    p=pow(r,l)
    s=s+p
    n=n//10
op=s
if ip==op:
    print('it is narcisstic number')
else:
    print('not narcisstic number')

1st que=STORE SQUARE OF LIST
l=[1,2,3,4,5]
print(l)
l1=[]
for i in l:
    s=i*i
    l1.append(s)
print(l1)    

2nd que=LIST CONTAINS INT,FLOAT,STR
l=[1,2,3,'omkar','parth','nik',20.5,40.4,60.8]
I=[]
s=[]
f=[]
for i in l:
    if type(i)==int:
        I.append(i)
    elif type(i)==str:
        s.append(i)
    elif type(i)==float:
        f.append(i)
print(I)
print(s)
print(f)

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
n=a.reshape(3,3)
print(n)
print(sum(n))
       
#DAY 4
1st que=MAX OF THREE NUMBERS
def max(a,b,c):
    if a>b:
        if a>c:
            print('max no is:',a)
        else:
            print('max no is:',c)
    elif b>c:
        print('max no is:',b)
    else:
        print('max no is:',c)
print(max(15,25,10))
print(max(10,6,7))
print(max(1,2,3))

5th que=RETURN LIST WITH UNIQUE ELEMENTS
def unique(l):
    s=set(l)
    return sorted(s)
print(unique([11,22,22,33,33,33,44,55,55,66]))

6th que=ADDITION OF 1ST and LAST digit
def sum(n):
    l=list(str(n))
    l1=l[0]+l[-1]
    s=0
    for i in l1:
        d=int(i)
        s=s+d
    return s
n=int(input('enter the number:'))
print(sum(n))    

4th que=SHOWSTUDENT FUNCTION
def showstudent(sname,sid=1,cname='VITA'):
    return sname,sid,cname
print(showstudent('omkar',20,'MET'))
print(showstudent('omkar'))

3rd que=SUM OF NUMBER USING RECURSION
def sum(n):
    if n==0:
        return n
    return n + sum(n-1)
n=int(input('enter the number:'))
print(sum(n))

2nd que=COUNT LOCAL VARIABLE IN FUNCTION
a=10
def fun():
    a=10
    b=20
    return len(locals())
print(fun())    

#DAY5
4th que-CONCAT TWO LIST INDEX WISE
l1=['m','na','i','om']
l2=['y','me','s','kar']
op=''
i,j=0,0
while i<len(l1) and j<len(l2):
    op=op+l1[i]+l2[j]+' '
    i+=1
    j+=1
print(op.split())

5th que-CHECK LIST ELEMENT PRESENT IN DICTIONARY VALUE
l1=[47,64,69,37,76,83,95,97]
d={'john':47,'peter':64,'mahi':37,'maria':76}
l2=[]
for i in l1:
    for j in d.values():
        if i==j:
            l2.append(i)
print(l2)

1st que=BUBBLE SORT
l1=[10,4,15,23,0]
for i in range(len(l1)-1):
    for j in range(len(l1)-1):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print('sorted list:',l1)        

2nd que=LINEAR SEARCH
l=[1,2,3,4,5,6,2,8,9]
k=int(input('enter the number:'))
l1=[]
found=False
for i in range(0,len(l)):
    if l[i]==k:
        found=True
        l1.append(i)
if found==True:
    print('element found at index')
    for i in l1:
        print(i)
else:
  print('number not found:')

3rd que=BINARY SEARCH
l=[1,2,3,4,5]
k=int(input('enter the number:'))
found=False
low=0
high=len(l)-1
while low<=high and not found:
    mid=(low+high)//2
    if k==mid:
        found=True
    elif k>high:
        low=mid+1
    else:
        high=mid-1
if found==True:
    print('key is found')
else:
    print('key is not found')

#DAY6
5th que=ACEES KEY "HISTORY"
d={'class':{'student':{'name':'mike','marks':{'physics':70,'history':80}}}}
print(d.get('history',80))#1st method
a=d['class']['student']['marks']['history']#2nd method
print(a)

1st que=SWAP KEY AND VALUES
d={'omkar':20,'parth':4,'mangesh':21}
print(d)
a=d.keys()
b=d.values()
a,b=b,a
print(dict(zip(a,b)))

4th que=extend nested list with another list
l=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
l1=['h','i','j']
l[2][1][2].extend(l1)
print(l)

2nd que=SELECTION SORT
l=[15,2,20,4,1]
for i in range(len(l)):
    m=min(l[i:])
    ind=l.index(m)
    l[i],l[ind]=l[ind],l[i]
print('sorted list',l)    

3rd que=INSERTION SORT
l=[15,2,20,4,1]
for i in range(1,len(l)):
    c=l[i]
    pos=i
    while c<l[pos-1] and pos>0:
        l[pos]=l[pos-1]
        pos=pos-1
    l[pos]=c
print('sorted list',l)    
    
***DAY 7***
5th que=COMPOSITION EXAMPLE
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print('name of student is:',self.name)
        print('id of student is:',self.id)
s=Student('omkar',2002)
s.display()

4th que=COUNT REF VARIABLE
import sys
class Student:
    def __init__(self,name):
        self.name=name
s=Student('omkar')
print(s.name)
print(sys.getrefcount(s))

3rd que=AREA OF SHAPE
class Shape:
    area=0
    class Square:
        def __init__(self,length):
            self.length=length
        def area(self):
            print('area of square:',self.length*self.length)
s=Shape()
s1=s.Square(5)
s1.area()
print('shapes area:',s.area)

2nd que=AREA,PERIMETER OF CIRCLE
class Circle:
    def __init__(self,pi,radius):
        self.pi=pi
        self.radius=radius
    def area(self):
        print("area of cicle:",self.pi*(self.radius*self.radius))
    def perimeter(self):
        print("perimeter of cicle:",2*(self.pi*self.radius))   
c=Circle(3.14,8)
c.area()
c.perimeter()

import sys
class Customer:
    bname='UCO BANK'
    def __init__(self,name,balance=2000):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('your balance after deposit is:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('your account has insufficient balance')
            sys.exit()
        self.balance=self.balance-amt
        print('your balance after withdraw amt:',self.balance)
print('WELCOME TO OUR BANK:',Customer.bname)
name=name=input("enter your name:")
c=Customer(name)
while True:
    print('d-deposit\nw-withdraw\ne-exit')
    option=input('CHOOSE YOUR OPTION:')
    if option=='d' or option=='D':
        amt=float(input('enter your amount to deposit:'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('enter your amount to withdraw:'))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        sys.exit()
    else:
        print('choose valid option')
'''

***DAY 8***
3rd que=MULTIPLE INHERITANCE
class A:
    def m1(self):
        print('A')
class B():
    def m1(self):
        print('B')
class C(A,B):pass
c=C()
c.m1()

1st que=IMPLEMENT CONSTRUCTOR WITH VARIABLE ARGUMENTS
class A:
    def __init__(self,*args):
        print('sum is:',sum(args))     
a=A(1,2,3) 

4th que=OPERATOR OVERLOADING
class Operator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('addition of number is:',self.a+self.b)
o=Operator(10,20)
o.add()
o1=Operator('omkar','saple')
o1.add()

5th que=SQUARE AND CUBE OF LIST USING LAMBDA
l=[1,2,3,4,5,6,7,8]
s=list(map(lambda n:n*n,l))
c=list(map(lambda n:pow(n,3),l))
print(s)
print(c)
'''
***DAY 9***
1st que=EXCEPTION HANDLING
def div(n):
    try:
       print(n//0)
    except ZeroDivisionError:
            return n%10
print(div(2))            

2nd que=MOB NO IS VALID OR NOT
import re
s=input('enter the mobile no:')
n=re.fullmatch('[6-9][0-9]{9}',s)
if n!=None:
    print('mob no is valid')
else:
    print('mob no is not valid')

3rd que=VALID MAIL ID OR NOT
import re
s=input('enter maild id:')
p=re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.]com',s)
if p!=None:
    print('its a valid mail id')
else:
    print('its not valid mail id')

4th que=VALID CAR NO OR NOT
import re
s=input('enter car registration number from state maharashtra:')
p=re.fullmatch('MH[0-9]{2}-[A-Z]{2}-[0-9]{4}',s)
if p!=None:
    print('valid car no')
else:
    print('not valid no')

5th que=ARITHMETIC OPERZTIONS USING DECORATOR
def arithmeticop(func):
    def op(a,b):
        func(a,b)
        print("The product is :", a*b)
        print("The division is :", a/b)
        print("The remainder is :", a%b)
    return op
@arithmeticop
def add_sub(a, b):
    print("The addition is :", a+b)
    print("The subtraction is :",a-b)
add_sub(8,4)

6th que=USING GENERATOR PRINT FIBONACCI
def fibo(n):
    a=0
    b=1
    for i in range(0,n):
        yield a
        a,b=b,a+b
for i in fibo(100):
    print(i)
'''
***DAY 10***
1st que-PRINT NUMPY VERSION
import numpy as np
print(np.__version__)

3rd que=NONO OF ARRAY ELEMENT IS ZERO 
import numpy as np
a=np.array({1,2,3])
print(np.all(a))

4th que=CHECK FOR NON ZERO ELEMET
import numpy as np
a=np.array([1,2,34,0])
print(np.any(a))

5th que=CHECK NAN IN ARRAY
import numpy as np
a=np.array([2,3,4,np.nan,5])
print(np.isnan(a))

6th que=COMPARE 2 ARRAYs
import numpy as np
a=np.array([1,20,34,2])
b=np.array([20,9,6,5])
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

7th que=CHECK 2 ARRAYS ARE EQUALS OR NOT
import numpy as np
x=np.array([72,79,85,90,150,-135,120,-10,60,100])
y=np.array([72,79,85,90,150,-135,120,-10,60,10.000001])
print(x==y)
print(x!=y)

8th que=GIVE THE SIZE OF ARRAY
import numpy as np
a=np.array([1,7,13,105])
print(np.size(a))

9th que=CREATE ARRAY OF 10ZEROS,10ONES,10FIVES
import numpy as np
a=np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5])
print(a)

10th que=CREATE ARRAY OF 30-70 INTEGERS
import numpy as np
a=np.arange(30,71)
print(a)

11th que=CREATE ARRAY OF EVEN INTEGERS FROM 30-70
import numpy as np
a=np.arange(30,71,2)
print(a)

12th que=CREATE 3*3 MATRIX
import numpy as np
a=np.arange(30,39)
print(a.reshape(3,3))

13th que=GENERATE RANDOM NO FROM 0,1
import numpy as np
print(np.random.normal(0,1))

14th que=GENERATE 15 RANDOME NOS
import numpy as np
print(np.random.normal(0,1,15))

15th que=CREATE VECTOR FROM 15-56 AND PRINT ALL NOS EXCEPT FST AND LAST
import numpy as np
a=np.arange(15,56)
print(a[1:41])

2nd que=CHECK ELEMETS ARE REAL,COMPLEX or SCALAR
import numpy as np
a=np.array([1,2,3,4+5j,10,2+3j,6+8j])
print(np.isreal(a))
print(np.iscomplex(a))
print(np.isscalar(a))
'''
***DAY 11***
1st que=CREATE ARRAY OF 3*4 AND ITERATE IT
import numpy as np
ar=np.arange(1,13)
ar=ar.reshape(3,4)
print(ar)
for i in np.nditer(ar):
    print(i)

2nd que=CREATE NUMPY ARRAY OF SIZE 10 AND EVENLY DISTRIBUTED BETWEEN 5-50
import numpy as np
a=np.linspace(5,50,10)
print(a)

3rd que=CHANGE SIGN OF ARRAY ELEMENT FROM 9,15
import numpy as np
a=np.arange(0,21)
print(a)
a[(a>=9) & (a<=15)]*=-1
print(a)

4th que=CREATE VECTOR LENGTH OF 5 AND FILLED WITH INTEGER 0-10
import numpy as np
b=np.random.randint(0,11,5)
print(b)

5th que=multiply 2 vectors
import numpy as np
a1=np.arange(1,10)
a2=np.arange(11,20)
print(a1*a2)

6th que=CREATE MATRIX OF 3*4 VALUES RANGE FROM 10-21
import numpy as np
a1=np.arange(10,22).reshape(3,4)
print(a1)

7th que=FIND NUMBER OF ROWS AND COLUMNS OF ARRAY
import numpy as np
a1=np.arange(10,22).reshape(3,4)
print(a1.shape)

8th que=IDENTITY MATRIX OF 3*3
import numpy as np
print(np.identity(3,dtype=int))

9th que=CREATE ARRAY WITH 1 ON BORDER AND INNER ELEMENTS ARE 0
import numpy as np
a=np.ones((10,10))
a[1:-1,1:-1]=0
print(a)

10th que=CREATE 5*5 MATRIX WITH DIAG ELEMENTS 1-5
import numpy as np
print(np.diag([1,2,3,4,5]))

11th que=CREATE ARRAY WITH DIAG ELEMTS 0 AND OTHERS 1
import numpy as np
a=np.zeros((4,4))
a[::2,1::2]=1
a[1::2,::2]=1

12th que=CREATE 3*3*3MATRIX 
import numpy as np
x = np.arange(0,27).reshape((3, 3, 3))
print(x)

13th que=CALCULATE SUM OF ELEMETS,ROW WISE,COLUMN WISE SUM
import numpy as np
a1=np.arange(10,22).reshape(3,4)
print(a1.sum())
print(a1.sum(axis=0))
print(a1.sum(axis=1))

14th que=INNER PRODUCT OF TWO VECTORS
import numpy as np
a1=np.array([2,3,4])
a2=np.array([6,7,8])
print(np.dot(a1,a2))

15th que=ADD VECTOR IN EACH ROW OF MATRIX
import numpy as np
a=np.arange(0,6).reshape(2,3)
print(a)
v=np.array([1,2,3])
r=np.empty_like(a)
for i in range(2):
    r[i]=a[i]+v
print(r)






