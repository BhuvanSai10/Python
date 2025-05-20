from collections import Counter

def countFreq(l):
    freq={}
    for i in l:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    return freq

print(countFreq([1,2,2,3,4,5,4]))
print(dict(Counter([1,2,2,3,4,5,4])))