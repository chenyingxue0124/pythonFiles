a = [0,3,3,7,5,3,11,1,3,1]
L = []
tmp = 0
for i,num in enumerate(a):
    L.append([num,i])
L.sort()
for n in range(len(L)-1):
    if L[n][0] != L[n+1][0]:
        tmp = max(tmp,abs(L[n][1]-L[n+1][1]))

print(tmp)