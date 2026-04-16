def fibonacci_generator(n):
    a, b =0,1
    for i in range(n):
        yield a 
        a, b =b,a+b  

n =int(input("how many terms:"))
gen =fibonacci_generator(n)

print("fibonacci series:")
for i in range(n):
    print(next(gen), end=" ")
    