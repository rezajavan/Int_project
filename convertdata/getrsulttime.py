import numpy as np

import matplotlib.pyplot as plt
from  scipy import signal
def getdatatime():

    f = open('media/file/test.bin', "rb")

    readfile = np.fromfile(f, dtype=np.uint16)

    data = []
    data2 = []
    Y = []


    for i in range(len(readfile)):

        data.append(readfile[i])

    base = 32768

    for i in range(len(data)):

        if data[i] >= base :

            c = base - data[i]



            data2.append(c)
        else :

            c = data[i]


            data2.append(c)

    n = len(data2)
    n = n/2
    n = int(n)
    m = 0
    for i in range(n):

        p = (data2[m]**2)  + (data2[m+1]**2)
        p = p**(1/2)
        Y.append(p)
        m = m + 2


    fs = 5.76*(10**6)
    isamplaefrequency = 1/fs
    X = np.linspace(0, isamplaefrequency*(len(Y)), len(Y))


    return X,Y




