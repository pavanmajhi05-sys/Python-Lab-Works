def sum_of_digits(n):
    total =0 #store sum Here....
    while n>0:
        digit =n% 10
        total =total+digit
        n=n //10

    print("Sum Of Digits:",total)
n=int(input("Enter A Number:"))
sum_of_digits(n)

