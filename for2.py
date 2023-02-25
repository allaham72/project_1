tup = (10, 20, -20, 2.4)


found = False
for t in tup:
    if t == 2.4:
        found = True
        break
    if t == -20:
        continue
    print(t)
if found == True:
    print("founded")
else:
    print("notfounded")
