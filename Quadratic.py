import math

def quadratic_roots(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        return (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)
    elif d == 0:
        return (-b / (2*a),)
    else:
        return None

if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    roots = quadratic_roots(a, b, c)
    if roots:
        print("Roots:", roots)
    else:
        print("No real roots")