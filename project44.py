

f = open("PIC_4913.JPG", 'rb')

f1 = open("PICmy.JPG", 'wb')
for i in f:
    f1.write(i)
