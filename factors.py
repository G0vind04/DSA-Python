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


