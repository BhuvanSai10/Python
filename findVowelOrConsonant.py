def findVowelOrConsonant(c):
    if c.isalpha():
        if c in ['a','e','i','o','u']:
            print("Vowel")
        else:
            print("Consonant")   
    else:
        print("Enter a single alphabet !") 
    
c = input()

findVowelOrConsonant(c)