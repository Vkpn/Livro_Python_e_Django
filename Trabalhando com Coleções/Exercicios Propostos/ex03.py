import math

N = int(input("Qual o valor limite: "))
A = list(range(2, N))
for i in range(2, int(math.sqrt(N) + 1)):
    if i in A:
        for j in range(i ** 2, N, i):
            if j in A:
                A.remove(j)
print(A)
