import numpy as np
import matplotlib.pyplot as plt

def getdata():
    f = open('media/file/test.bin', "rb")



    readfile = np.fromfile(f, dtype=np.int16)

    data = []
    data2 = []
    realpart = []
    imagepart = []

    for i in range(len(readfile)):

        data.append(readfile[i])

    base = 32768

    for i in range(len(data)):

        if data[i] >= base :

            c = base - data[i]
            c = c/base



            data2.append(c)
        else :

            c = data[i]/base

            data2.append(c)




    n = len(data2)
    n = n/2
    n = int(n)
    m = 0
    for i in range(n):
        realpart.append(data2[m])
        imagepart.append(data2[m+1])
        m = m + 2

    return realpart,imagepart


