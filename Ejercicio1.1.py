def countingSort(A, k):
    C = [0 for _ in range(k + 1)]
    B = [0 for _ in range(len(A))]
    
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B

def dinamico(A):
    k = max(A)
    if not (10 < k < 30):
        print(f"Error")
    return k

A = [27, 9, 28, 10, 3, 15, 0, 2, 17, 22]
k = dinamico(A)
B = countingSort(A, k)

print("k: ", k)
print("Lista desordenada: ", A)
print("Lista ordenada: ", B)
