A = [1, 2, 4, 6]
B = [2, 3, 6]
C = []
i = 0
j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
     C.append(B[j])
     j += 1
while i < len(A):
    C.append(A[i])
    j += 1
while j < len(B):
    C.append(B[i])
    j = j + 1
    print(C)







