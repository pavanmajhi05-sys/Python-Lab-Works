def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

S = "Durga Chandu Peddinti"
print("The reversed string is: ", end="")
print(reverse(S))
