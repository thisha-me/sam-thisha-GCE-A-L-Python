import sys

L = input('Enter int list :')
K = int(input('Enter K'))
L = L.split(' ')

for i in range(0, len(L)):
    L[i] = int(L[i])

N = len(L)
X = sys.maxsize  # or yu can use any resanoble x number
a = 0

while(a < N):
    if (L[a] > K):
        if(L[a] < X):
            X = L[a]
    a = a+1
print(X)
