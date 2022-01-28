a = 1
b = 2
c = 3
x = 0

if a < b:
    x = x + a
else:
    x = x + b
if b > c and a <= b:
    x = x + c
else:
    x = x + a
if a <= b and a <= c:
    x = x + a
if b < c or c < a:
    x = x + c

print(x)