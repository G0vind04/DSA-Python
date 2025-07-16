#introduction to hashing-- how to store frequency in a dictionary

num=[5,6,7,7,1,9,11,1,5,1,1]
freq_map={}
for i in range(len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1
print(freq_map)