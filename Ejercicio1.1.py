def countingSort(A, k):
    C=[0 for _ in range(k + 1)]
    B=[0 for _ in range(len(A))]
    for j in range(0,len(A)):
        C[A[j]]= C[A[j]]+1

    for i in range(1, k + 1):
        C[i]=C[i]+C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]]= C[A[j]]-1
    return B

datos = [14, 3, 20, 0, 7, 14, 18, 2, 7, 11]
k = max(datos) #k dinamico

resultado = countingSort(datos, k)
print("Lista desordenada:", datos)
print("Lista ordenada:", resultado)
