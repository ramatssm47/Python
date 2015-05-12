
import csv,os
import matplotlib.pyplot as plt 
from datetime import datetime
import StringIO
import urllib, base64
from django.http import HttpResponse



def outputList(filePath):
    count=0
    dataList=[]
    with open(filePath, "r") as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            dataList.append(row)
            count=count+1  
        return dataList
    
def plot1(filePath,name,type):
    count = 0
    x1 = []
    f = []
    with open(filePath, "r") as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            count+=1
            if type=="open":
                x1.append(float(row[1]))
            elif type =="high":
                x1.append(float(row[2]))
            elif type =="low":
                x1.append(float(row[3]))
            elif type =="close":
                x1.append(float(row[4]))
            
            f.append(datetime.strptime(row[0], "%Y-%m-%d").date())
    
    
    imgf = open("chart1.png", "w")
    fig = plt.figure()
    plt.grid()
    name1 = "Stock value for "+ name;
    plt.title(name1,fontsize=12)
    plt.xlabel("Time Series Data")
    plt.ylabel("Stock Value")
    plt.plot(f,x1,'b-' ,label=name)
    
    #plt.plot((f[j1],f[j2],f[j3],f[j4],f[j5],f[j6]),(x1[j1],x1[j2],x1[j3],x1[j4],x1[j5],x1[j6]),'g-' , linewidth=4, label='MSFT')
    plt.legend(loc ='upper right',fontsize=8)
    #plt.savefig("chart1.png")
    imgf.close()
    print "chart saved"
    #os.startfile("chart1.png")
    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data
    plt.close()
    print "Content-type: image/png\n"
    uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata.buf))
    """
    print '<img src = "%s"/>' % uri

    html = '''\<html><head>
    <title>STI</title>
    </head>
    <body>
    <img src = "%s"/>''' %uri+'''
    </body>
    </html>
    ''' 
    """
    return uri


    