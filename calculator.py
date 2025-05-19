def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulo(a,b):
    return a%b

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))



print("Addition of a, b = "+str(add(a,b)))
print("Subtraction of a, b = "+str(subtract(a,b)))
print("Multiplication of a, b = "+str(multiply(a,b)))
print("Division of a, b = "+str(divide(a,b)))
print("Modulo of a, b = "+str(modulo(a,b)))