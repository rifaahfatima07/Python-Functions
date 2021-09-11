#swapping of files

f1 = open('Test.txt', 'r')
data1 = f1.read()
f2 = open('Test2.txt', 'r')
data2 = f2.read()

f3 = open('Test.txt', 'w')
f3.write(data2)
f4 = open('Test2.txt', 'w')
f4.write(data1)

