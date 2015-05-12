import csv,os
import matplotlib.pyplot as plt 
from datetime import datetime
from django.http import HttpResponse
import StringIO
import urllib, base64

def plot2(filePath1,filePath2,comp1,comp2,type):
  
    count = 0
    x1 = []
    f1 = []
    x2 = []
    f2 = []
    
    with open(filePath1, "r") as csvfile:
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
            
            f1.append(datetime.strptime(row[0], "%Y-%m-%d").date())
    
    with open(filePath2, "r") as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            count+=1
            if type=="open":
                x2.append(float(row[1]))
            elif type =="high":
                x2.append(float(row[2]))
            elif type =="low":
                x2.append(float(row[3]))
            elif type =="close":
                x2.append(float(row[4]))
            f2.append(datetime.strptime(row[0], "%Y-%m-%d").date())
                    
   
    ########### Chart Plot##################
    
    imgf = open("chart1.png", "w")
    fig = plt.figure()
    plt.grid()
    name1 = comp1 +" VS "+ comp2;
    plt.title(name1, fontsize=12, color='b');
    plt.xlabel("Time Series Data")
    plt.ylabel("Stock Value")
    plt.plot(f1,x1,'b-' , label=comp1)
    plt.plot(f2,x2,'g-' , label=comp2)
    plt.legend(loc ='upper right', fontsize=8)
    #plt.savefig("chart1.png")
    imgf.close()
    print "chart saved"
    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data
    plt.close()
    print "Content-type: image/png\n"
    uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata.buf))
    return uri
