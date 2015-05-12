import csv
import matplotlib.pyplot as plt 
from datetime import datetime
from array import *

i=0
x1 = []
y1 = []
"""
sum=0
l = (["MSFT", "IBM"])
for i in l:
    print l[sum]
    sum +=1

fil = raw_input("Please selcet the stock chart you want :  ")
filename = fil+".csv"
"""
"""
def chart_plot(filename):
    with open(filename, "rU") as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            row[1] = row[1].split(",")
            for val in row[1]:
                x1.append(float(val))
            row[2] = row[2].split(",")
            for val in row[2]:
                y1.append(float(val))
    cal = []

    f = []

    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            f.append(datetime.strptime(row[0], "%Y-%m-%d").date())
            while(i<7000):
                i += 1
                if((i%700) == 0):
                    cal.append(i)
        
    j1 = int(cal[1])
    j2 = int(cal[2])
    j3 = int(cal[2])
    j4 = int(cal[4])
    j5 = int(cal[5])
    j6 = int(cal[6])

    fig = plt.figure()
    #ax1 = fig.add_subplot(111)
    plt.grid()
    plt.title("Stock Value Comparison")
    plt.xlabel("Time Series Data")
    plt.ylabel("Stock Value")
    plt.plot((f[j1/2],f[j2/2],f[j3/2],f[j4/2],f[j5/2],f[j6/2]),(x1[j1],x1[j2],x1[j3],x1[j4],x1[j5],x1[j6]),'b-' ,label=fil)
    #plt.plot((f[j1],f[j2],f[j3],f[j4],f[j5],f[j6]),(x1[j1],x1[j2],x1[j3],x1[j4],x1[j5],x1[j6]),'g-' , linewidth=4, label='MSFT')
    plt.legend(loc ='upper right')
    plt.show()

chart_plot(filename)

if __name__ == '__main__':
    chart_plot()
"""
    
######First chart for comparision#####

with open("/home/dinesh/workspace/file.csv", "rU") as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        row[1] = row[1].split(",")
        for val in row[1]:
            x1.append(float(val))
        row[2] = row[2].split(",")
        for val in row[2]:
            y1.append(float(val))



cal = []

f = []

with open("/home/dinesh/workspace/file.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        f.append(datetime.strptime(row[0], "%Y-%m-%d").date())
        while(i<7000):
            i += 1
            if((i%100) == 0):
                cal.append(i)
        
j1 = int(cal[1])
j2 = int(cal[2])
j3 = int(cal[2])
j4 = int(cal[4])
j5 = int(cal[5])
j6 = int(cal[6])
"""
#####Second chart for comparision######

i1=0
x2 = []
y2 = []

fg = open("IBM.csv", "rU")
#    reader1 = csv.reader(csvfile)
#    reader1.next()
for row in fg:
    fg.next()
    row[1] = row[1].split(",")
    for val in row[1]:
        x2.append(float(val))
    row[2] = row[2].split(",")
    for val in row[2]:
        y2.append(float(val))
    


cal1 = []

f1 = []

fg = open("IBM.csv", "r")
#    reader = csv.reader(csvfile)
#   reader.next()
for row in fg:
    fg.next()
    f1.append(datetime.strptime(row[0], "%Y-%m-%d").date())
    while(k<7000):
            k += 1
            if((k%700) == 0):
                cal1.append(k)

k1 = int(cal1[1])
k2 = int(cal1[2])
k3 = int(cal1[2])
k4 = int(cal1[4])
k5 = int(cal1[5])
k6 = int(cal1[6])
"""
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.grid()
plt.title("Stock Value Comparison")
plt.xlabel("Time Series Data")
plt.ylabel("Stock Value")
plt.plot((f[j1/2],f[j2/2],f[j3/2],f[j4/2],f[j5/2],f[j6/2]),(x1[j1],x1[j2],x1[j3],x1[j4],x1[j5],x1[j6]),'b-' ,label='IBM')
#plt.plot((f[j1],f[j2],f[j3],f[j4],f[j5],f[j6]),(x1[j1],x1[j2],x1[j3],x1[j4],x1[j5],x1[j6]),'g-' , linewidth=4, label='MSFT')
plt.legend(loc ='upper right')
plt.show()


