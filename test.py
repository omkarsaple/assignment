'''
5th question
l1=[3,6,9,12,15,18,21]
o1=l1[1::2]
print(o1)
l2=[4,8,12,16,20,24,28]
o2=l2[0::2]
print(o2)
output=o1+o2
print(output)

1.1
d=int(input('enter your digit:'))
c=0
while d!=0:
    d=d//10
    c+=1
print(c)

1.2
l=[10,20,30,40,50]
print(l[::-1])

2.
s1='chrisdem'
s2='iamnewstring'
o1=int(len(s1)/2-1)
output=s1[0:o1]+s2+s1[o1::]
print(output)

3.
s='PyNaTive'
l=[]
c=[]
for i in s:
    if i.islower():
        l.append(i)
    else:
        c.append(i)
print(''.join(l+c))

nt(low+up)
'''
import re
s="'english'= 78 'science'= 83 'history'= 60"
op=(re.findall(r'\d\d',s))
s=list(map(int,op))
print("sum:",sum(s),"average:",sum(s)/len(s))

    
