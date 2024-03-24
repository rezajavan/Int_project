def hextobinary():

    file = "'media/file/test.bin'"

    f = open(file,mode='rb')

    hexdata = f.read()

    bindata = []
    bindata2 = []
    bindata3 = []
    bindata4 = []

    for i in range(len(hexdata)):

        bindata.append(bin(hexdata[i]))

    for i in range(len(bindata)):

        bindata2.append(bindata[i][2:10])
    for i in range(len(bindata2)):
        c = bindata2[i]

        c = "0"*( 8 - len(c)) + bindata2[i]
        bindata3.append(c)
        bindata4.append(c[::-1])


    return bindata4


def convertto16bit():

    data = hextobinary()

    data16bit = []



    n = len(data)/2
    n = int(n)

    m = 0
    for i in range(n):

        data16bit.append(data[m] + data[m+1])

        m = m + 2


    return data16bit



def bintofloat():
    datafloat = []

    data = convertto16bit()
    base = 2**15;

    for i in range(len(data)) :
        if data[i][0] == '0':

            c = int(data[i][1:16],2)
            c = c/base

            datafloat.append(c)



        if data[i][0] == '1':

            c = int(data[i][1:16], 2)
            c = c/base

            datafloat.append(c*-1)

    return datafloat


def converttocomplex():

    data = bintofloat()

    realpart = []
    imagepart = []


    n = len(data)/2
    n = int(n)
    m = 0
    for i in range(n):

        realpart.append(data[m])
        imagepart.append(data[m+1])

        m = m + 2


    return realpart,imagepart



def getdata():

    (re,ima) = converttocomplex()

    return re,ima











hextobinary()