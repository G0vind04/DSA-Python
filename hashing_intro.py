#introduction to hashing - 
#suppose we hve 2 lists n and m. check if content of m in n and count no of occurences
#constraints- 1<=n[i]<=10
#           - n can have 10**8 elem
#           - m can have 10**8 elem


#---------brute force----------------
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,11,1,9,5,67,2]
for i in m:
    count=0
    for x in n:
        if x==i:
            count+=1
    print(i,"=",count)
            
#--------optimal solution---------------
n1=[5,3,2,2,1,5,5,7,5,10]
m1=[10,11,1,9,5,67,2]
hash_list=[0]*11
for k in n1:
    hash_list[k]+=1
for k in m1:
    if k<0 or k>10:
        print(0)
    else:
        print(k,"=",hash_list[k])