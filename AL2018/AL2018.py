L = input('Enter List :')
K = int(input('Enter K :'))

L = L.split(',')
for i in range(len(L)):
    L[i] = int(L[i])

n = len(L)
i = 0

while i < n:
    if(L[i] == K):
        print('True')
        break
    i += 1
else:
    print('False')
