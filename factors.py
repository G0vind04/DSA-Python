#this is the brute force solution (least optimal)
#time complexity - 0(n)

num=int(input("enter a number"))
result=[]
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print(result)   


#better solution
#time complexity -0(n/2) or 0(n)

num1=int(input("enter a number"))
result1=[]
for i in range(1,num1//2+1):
    if num%i==0:
        result1.append(i)
result1.append(num)
print(result1)

#optimal solution
#time complexity 0(nlogn)+0(sqrt)n))
from math import sqrt
num2=int(input("enter the number"))
result2=[]
for i in range(1,int(sqrt(num2))+1):
    if num%i==0:
        result2.append(i)
        if num//i!=i:
            result2.append(num//i)
result2.sort()
print(result2)
