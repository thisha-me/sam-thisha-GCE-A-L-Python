X = 0
Y = [0, 0, 0]

file = open('Marks.txt', 'a')
while (X != -1):

    X = int(input('Enter Index No : '))
    if (X == -1):
        break

    for i in range(0, 3):
        Y[i] = input('Enter Marks : ')

    data = 'Index_no_{0},{1},{2},{3}\n'.format(X, Y[0], Y[1], Y[2])
    file.write(data)
file.close()
