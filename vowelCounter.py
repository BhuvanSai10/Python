def countVowels(s):
    v = 0
    for c in s:
        if c in  ['a','e','i','o','u']:
            v+=1
    
    return v

print(countVowels("bhuvansai"))