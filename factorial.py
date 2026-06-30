import math
X=0 
denominator=2
Numerator=1
for i in range(4):
    X += Numerator/math.factorial(denominator)
    Numerator *=2
    denominator *=2
print(X)
