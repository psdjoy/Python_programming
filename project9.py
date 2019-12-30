from math import pow

x = [6, 8, 12, 14, 18]
y = [350, 775, 1150, 1395, 1675]

X = 0       # average of x
Y = 0       # average of y
XY = 0      # average of x*y
X2 = 0      # average of x^2
X3 = 0      # square of (average of x)
for i in range(5):
    X = X + x[i]
    Y = Y + y[i]
    XY = XY + x[i]*y[i]
    X2 = X2 + pow(x[i], 2)
    if i == 4:
        X = X / 5
        Y = Y / 5
        XY = XY / 5
        X2 = X2 / 5
        X3 = pow(X, 2)

m = (X*Y - XY)/(X3 - X2)
c = Y - m*X
print('X', X)
print('Y', Y)
print('XY', XY)
print('Average of x^2', X2)
print('Square of (average of x)', X3)
print('M', m)
print('C', c)
print('y = ', m, 'x', c)
