def factorial(n):
    result =1
    i=1
    while i <= n:
        result = result*i
        i += 1
    return result

def calculate_x():
    x =0

    numerator =1
    denominator =2    

    for i in range(4):
        term = numerator/factorial(denominator)
                                   
        x=x +term
        print("term",i+1,"=",term)
        numerator = numerator*2
        denominator = denominator *2

    print("final X=",x)
calculate_x()