def reverse(s):
    i = len(s) - 1
    rev=""
    while(i>=0):
        rev = rev + s[i]
        i = i-1
    
    return rev

print(reverse("bhuvansai"))
