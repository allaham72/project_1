import numpy as np
a = []
for i in range(10):
    a1 = int(input("write 10 numbers: "))
    a.append(a1)
y = np.array([
    [a[0], a[1]], [a[2], a[3]]
])
x = np.array([
    [a[4], a[5]], [a[6], a[7]], [a[8], a[9]]
])
vv=np.dot(x, y)
print(vv)