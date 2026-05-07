
n1 = 0
n2 = 1

for fibonacci in range(0, 9):
    sequencia = (n1, n2) = (n2, n1 + n2)

    print(n1)
