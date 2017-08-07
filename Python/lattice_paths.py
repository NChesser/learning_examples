
def lattice(n):
    ret = 1
    for j in range(1, n+1):
        ret *= n + j
        ret //= j
    return ret

print(lattice(20))