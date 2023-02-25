index = 8
a = [0, 1]
i = 2
while i < index:
    a.append(a[i-1]+a[i-2])
    i = i+1
    print(a)