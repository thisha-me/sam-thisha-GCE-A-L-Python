homeNo = input('Enter Home Number :')
lastRead = int(input('Enter Last Read :'))
currentRead = int(input('Enter Current Read :'))

unit = currentRead-lastRead
if (unit <= 64):
    charge = 5*unit
else:
    charge = (64*5)+10*(unit-64)

print(charge)


def writeData(homeNo, lastRead, currentRead, charge):

    file = open("deb.txt", 'a')
    file.write('{0}, {1}, {2}, {3}\n'.format(
        homeNo, lastRead, currentRead, charge))
    file.close()
