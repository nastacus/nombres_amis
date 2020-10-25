from random import*
print("Ce programme génére deux nombres de 3 chiffres et vérifie s'ils sont amis")
m=randint(100,999)
n=randint(100,999)
while m==n :
    n=randit(100,999)
S1=S2=0
if(m>n) :
    maxx=m
    minn=n
else :
    maxx=n
    minn=m
for i in range(1,maxx):
    if maxx % i==0 :
        S1=S1+i
    if(i<minn-1)and(minn%i==0) :
        S2=S2+i
if(S1==minn)and(S2==maxx):
    print(m,"et",n,"sont amis")
else :
    print(m,"et",n,"ne sont pas amis")