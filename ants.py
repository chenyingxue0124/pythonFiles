L = 100
n = 20

def solve(x):
    min_T = 0
    for i in range(0, n-1):
        min_T = max(min_T, min(x[i], L - x[i]))

    max_T = 0
    for i in range(0, n-1):
        max_T = max(max_T, max(x[i], L - x[i]))

    return min_T, max_T

print(solve(4))