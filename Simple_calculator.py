def add(a,b):
    return a+b 
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b ==0:
        return "Error connot divided by Zero"
    else:
        return a/b
print ("=== Simple Calculator ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == '4':    print(num1,"/",num2,"=",divide(num1,num2))
else:    print("Invalid input") 

