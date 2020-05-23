***day 1***
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
'''
4th ques=row wise sum
def row_sum(n):
    n=pow(n,3)
    return n
print(row_sum(2))
print(row_sum(4))
