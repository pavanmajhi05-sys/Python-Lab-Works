def pascal_triangle (n) :
    for i in range (n) :
        num = 1
        print (' ' *(n-i) , end= ' ')
        for j in range (1 , i + 1) :
            num = num * (i - j + 1) // j
            print (num , end= ' ')
        print ()


if __name__ == '__main__':
    try:
        n = int(input('Enter the number of rows for Pascal triangle: '))
        pascal_triangle(n)
    except ValueError:
        print('Please enter a valid integer.')
