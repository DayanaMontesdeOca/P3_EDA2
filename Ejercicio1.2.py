def countingSort(A, k): #descendente
    C = [0 for _ in range(k + 1)]
    B = [0 for _ in range(len(A))]
    
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
 
    for i in range(k - 1, -1, -1):  #suma acumulada de derecha a izquierda
        C[i] = C[i] + C[i + 1]  #suma el elemento posterior

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B

k = 29
datos = [27, 9, 28, 10, 3, 15, 0, 2, 17, 22]

resultado = countingSort(datos, k)
print("Lista desordenada:", datos)
print("Lista ordenada:", resultado)
