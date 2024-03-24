from django.db import connection

from .form import BookForm
import convertdata.getrsulttime as bindatatime
import matplotlib.pyplot as plt
import io
import convertdata.getresult as binfile
import convertdata.getresultsspec as getspec
import base64
from django.shortcuts import render,redirect , HttpResponse
import numpy as np

def upload(request):


    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES.get('file')
            readfile = f.read()
            file = open('media/file/test.bin', 'wb')
            file.write(readfile)
            file.close()











            return redirect('choose')




    else:
        form = BookForm()

    return render(request, 'app1/upload.html', {'form': form})




def show(request):
    if request.method == 'POST':
        plt.rcParams['agg.path.chunksize'] = 8192
        if "Spectrogram" in request.POST:
            window = request.POST['window-sp']
            (t, f, Sxx) = getspec.getpicspec(window)
            plt.rcParams['agg.path.chunksize'] = 8192
            fig, axe2 = plt.subplots(1)
            axe2.set_xlabel('Time(msec)' , color = 'b' ,size = 10)
            axe2.set_ylabel("frequency(MHz)", color = 'b' ,size = 10)
            axe2.set_title('spectrogram'  , color = 'r' , size = 20)
            axe2.grid('on')
            im = axe2.pcolormesh(t,f,Sxx, cmap='plasma')
            fig.colorbar(im, ax=axe2 )
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=300 , bbox_inches='tight' ,   pad_inches = 0.01)
            image2 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            plt.cla()
            buf.close()
            size = "100%"
            return render(request, 'app1/show.html', { 'image': image2 , "size": size})
        if "Scatter plot" in request.POST:
            ############image0
            fig, axe0 = plt.subplots(1)
            (X,Y) = binfile.getdata()
            axe0.set_facecolor('darkgrey')
            axe0.set_title('Scatter plot' , color = 'r' , size = 20)
            axe0.set_xlabel('Real part ' ,color = 'b' , size = 10)
            axe0.set_ylabel('Image part' , color = 'b' ,size = 10)
            plt.rcParams['agg.path.chunksize'] = len(X) * 4

            axe0.scatter(X, Y, s = 4 ,color='b')
            axe0.grid('on')


            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=300 , bbox_inches='tight' ,  pad_inches = 0.01)
            image0 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            plt.cla()
            buf.close()
            size = '50%'
            return render(request, 'app1/show.html', {'image': image0 , "size":size})
            ###########
            ####image1
        if "Domain Time" in request.POST:
            fig, axe1 = plt.subplots(1)
            (X,Y) = bindatatime.getdatatime()
            X =X * 1000
            #plt.rcParams['backend'] = 'TkAgg'
            plt.rcParams['agg.path.chunksize'] = 8192



            axe1.set_facecolor('darkgrey')
            axe1.set_title('Time domain signal'  , color = 'r' , size = 20)
            axe1.set_xlabel('Time(msec)' , color = 'b', size = 10)
            axe1.set_ylabel('Absolute value' , color = 'b', size = 10)
            axe1.plot(X,Y,  linewidth = 0.15)
            axe1.grid('on')
            #io.DEFAULT_BUFFER_SIZE = 65536
            buf = io.BytesIO()

            plt.savefig(buf, format='png', dpi=300 , bbox_inches='tight' ,   pad_inches = 0.3)
            image1 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            plt.cla()
            buf.close()
            size = '100%'
            return render(request, 'app1/show.html', {'image': image1 , "size":size})
            ##################
            ########image2

        if "welch" in request.POST:



            window = request.POST['window-welch']
            (f, Pxx_den)  = getspec.getpicwl(window)


            fig, axe3 = plt.subplots(1)
            axe3.set_facecolor('darkgrey')
            axe3.set_xlabel('frequency (MHz)' , color = 'b' ,size = 10)
            axe3.set_ylabel('PSD (V^2/Hz)', color = 'b' ,size = 10)
            axe3.set_title('PSD'  , color = 'r' , size = 20)
            axe3.semilogy(f, Pxx_den)
            axe3.grid('on')

            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=300 , bbox_inches='tight' ,   pad_inches = 0.01)
            image3 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            plt.cla()
            buf.close()
            size = '50%'
            return render(request, 'app1/show.html', { 'image': image3 , "size": size})



    else:
        return render(request, 'app1/choose.html')


def nbiot(request):
    if request.method == 'POST':

        if request.POST['mode'] == "0":
           mod = "inband"
           ltep = request.POST["lteport" ]
           if ltep == '0' :
               ltep = '1'
           txn =  request.POST["tx"]
           nbid = request.POST['nbiotid']
           nbi = nbid
           nbid = int(nbid)
           nbport = request.POST['nbiotport']
           nbp = nbport
           if nbid % 3 == 0:
               nbidt = "1"

           if nbid % 3 == 1:
               nbidt = "2"

           if nbid % 3 == 2:
               nbidt = "3"

           addodd = "../../static/app1/pic" + ltep + txn + "0" + "2" + nbidt + "1" + nbport + ".jpg"
           addeven = "../../static/app1/pic" +  ltep + txn + "0" + "2" + nbidt + "2" + nbport + ".jpg"

           return render(request, 'app1/nbiot.html',
                         {'addresodd': addodd, 'addreseven': addeven, "nbp": nbp, "nbi": nbi, "mod": mod, "ltp":'l'+ltep ,"tn" : "tx"+txn})


        if request.POST['mode'] == "1":
            mod = "Guardband"
            nbid = request.POST['nbiotid']
            nbi = nbid
            nbid = int(nbid)
            nbport = request.POST['nbiotport']
            nbp = nbport
            if nbid%3 == 0:
                nbidt = "1"

            if nbid%3 == 1:

                nbidt = "2"

            if nbid%3 == 2:

                nbidt = "3"

            addodd = "../../static/app1/pic" + "2" +  nbidt + "1" + nbport + ".jpg"
            addeven = "../../static/app1/pic" + "2" + nbidt + "2" + nbport + ".jpg"

            return  render(request,'app1/nbiot.html' ,
                           {'addresodd' : addodd , 'addreseven':addeven , "nbp" : nbp , "nbi":nbi , "mod":mod} )



    else:
        nbp = 0
        nbi = 0
        mod = "Guardband"

        addodd = "../../static/app1/pic" + "2" + '1' + "1" +'0'+ ".jpg"
        addeven = "../../static/app1/pic" + "2" + '1' + "2" + '0' + ".jpg"

        #return render(request, 'app1/nbiot.html' ,{'addresodd' : addodd , 'addreseven':addeven,"nbp" :nbp , "nbi":nbi ,'mod':mod  })
        return render(request, 'app1/nbiot.html' , {'addresodd' : addodd , 'addreseven':addeven})

def nbiott(request):


    addodd = "../../static/app1/pic" + "2" + '1' + "1" + '0' + ".jpg"
    addeven = "../../static/app1/pic" + "2" + '1' + "2" + '0' + ".jpg"


    return render(request, 'app1/nbt.html', {'addresodd': addodd, 'addreseven': addeven})