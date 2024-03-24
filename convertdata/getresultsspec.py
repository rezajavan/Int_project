import math

import numpy as np

import matplotlib.pyplot as plt
from  scipy import signal

def getpicspec(window):
    plt.cla()
    fop = open('media/file/test.bin', "rb")

    readfile = np.fromfile(fop, dtype=np.int16)

    data = []
    data2 = []
    Y = []

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
        p = np.complex(data2[m],data2[m+1])
       # p = (data2[m]**2)  + (data2[m+1])
       # p = p**(1/2)
        Y.append(p)
        m = m +2




    fs = 5.76 * (10 ** 6)



    x = np.array(Y)





    f, t, Sxx = signal.spectrogram(x, fs=fs, window=window ,nfft=384,noverlap=98,return_onesided=False,mode='psd')
    t = t *1000
    f = f / (10 ** 6)



    #plt.pcolormesh(t,np.fft.fftshift(f,axes=0),np.fft.fftshift(Sxx, axes=0),cmap='plasma')
    #plt.pcolormesh(t,f,Sxx,cmap='plasma')
    #plt.show()

    return t , f , Sxx













def getpicwl(window):
    plt.cla()
    f = open('media/file/test.bin', "rb")

    readfile = np.fromfile(f, dtype=np.uint16)

    data = []
    data2 = []



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

    Y = data2













    fs = 5.76 * (10 ** 6)



    x = np.array(Y)
    plt.axis('on')

    f, Pxx_den = signal.welch(x ,fs=fs,window=window)

    f = f / (10 ** 6)


    #plt.semilogy(f, Pxx_den)
    #plt.show()



    return f,Pxx_den




