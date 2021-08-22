n = int(input('Enter n :'))
a = 0

while(not(n <= 0)):
    x = int(input('Enter x :'))
    if(x % 2 == 0):
        a = a+1
    n = n-1
print(a)
