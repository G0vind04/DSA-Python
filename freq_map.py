#introduction to hashing-- how to store frequency in a dictionary

num=[5,6,7,7,1,9,11,1,5,1,1]
freq_map={}
for i in range(len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1
print(freq_map)

#using hashmaps get

num1=[5,6,7,7,1,9,11,1,1,5,1,1]
hash_map={}
n=len(num)
for i in range(n):
    hash_map[num[i]]=hash_map.get(num[i],0)+1
print(hash_map)