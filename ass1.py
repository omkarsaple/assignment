***DAY 1***
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
***DAY 2***
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
***DAY 3***
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
       
***DAY 4***
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

***DAY5***
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
'''
***DAY 6***
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
'''    
