# def swap(a,b):
#     return b,a

def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))

a,b = swap(a,b)

print("a = ",a)
print("b = ",b)