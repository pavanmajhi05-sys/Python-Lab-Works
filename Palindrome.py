def palindrome_check(n):
    original = str(n)
    reverse =original[: :-1]

    if original==reverse:
        print(n, "is a polindrome")
    else:
        print(n, "Not a polindrome")

n=int (input("Enter a Number :"))            
palindrome_check(n)