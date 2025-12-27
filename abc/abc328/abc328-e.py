# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))

s=list(input())
t=list()
if s[0]=='A':
    c=1
if s[0]=='B':
    c=2
if s[0]=='C':
    c=3   
flg=0 
for i in range(1,len(s)):
    if s[i]=='A' and s[i-1]<s[i]:
        c+=1
        flg=0
    elif s[i]=='A':
        t.append(c)
        c=1
        flg=1
    elif s[i]=='B' and s[i-1]<s[i]:
        c+=2
        flg=0
    elif s[i]=='B':
        t.append(c)
        c=2
        flg=1
    if s[i]=='C' and s[i-1]<s[i]:
        c+=4
        flg=0
    elif s[i]=='C':
        t.append(c)
        c=4
        flg=1

t.append(c)
print(t)
def seven(text,num,pls):
    ans=num
    if num==0 and text[pls]==7:
        ans=seven(text,num+1,pls)
    elif pls-num>0 and pls+num<len(text):
        if text[pls+num]+text[pls-num]==7:
            ans=seven(text,num+1,pls)
    return ans

flg=[True for i in range(len(t))]
for i in range(len(t)):
    counter=seven(t,0,i)
    for j in range(counter):
        flg[i-j]=False
        flg[i+j]=False

new=list()
for i in range(len(t)):
    if flg[i]:
        new.append(t[i])

cursor=0
fin=list()
flg3=0
while cursor<len(new)-2:
    if new[cursor]+new[cursor+1]+new[cursor+2]!=7:
        flg3=0
        fin.append(new[cursor])
        cursor+=1
    else:
        flg3=1
        cursor+=3
if (flg3==0 and cursor==len(new)-2):

    fin.append(new[cursor])
    fin.append(new[cursor+1])
if (flg3==0 and cursor==len(new)-1):

    fin.append(new[cursor])
elif flg3==1 and cursor==len(new)-2:

    fin.append(new[cursor])
    fin.append(new[cursor+1])
elif flg3==1 and cursor==len(new)-1:

    fin.append(new[cursor])

inter=str()
for i in fin:
    if i==1:
        inter+='A'
    elif i==2:
        inter+='B'
    elif i==3:
        inter+='AB'
    elif i==4:
        inter+='C'
    elif i==5:
        inter+='AC'
    elif i==6:
        inter+='BC'
print(inter)