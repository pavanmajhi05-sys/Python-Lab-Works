def generate_n_chars(n, c):
    result = ""
    for i in range(n):
        result += c
    return result

inputChar = input("Enter the character:")
inputNum = int(input("Enter the number of times" + str(inputChar) + "to be printed:"))
print("Result:" + str(generate_n_chars(inputNum, inputChar)))
