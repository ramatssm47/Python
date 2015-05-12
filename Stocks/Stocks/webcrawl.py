import urllib
import os
import re
import webbrowser
import csv

def webcrawl():
    sum=0
    l = (["MSFT", "IBM"])
    for i in l:
        print l[sum]
        sum +=1
    
    chartval = raw_input("Please selcet the stock chart you want :  ")
    filename = chartval+".csv"
    fil = open(chartval+".csv", "w")
    fil.close()
    print chartval
    target = "http://ichart.yahoo.com/table.csv?s="+chartval


    print target
    wrlopen = urllib.urlopen(target)
    #urllib.urlretrieve(target,"MSFT.csv")
    t = webbrowser.open_new(target)



    conf = raw_input("Do you want to proceed y/n : ")
    if conf == 'y':
        print "Stock table has been downloaded"
        f = csv.writer(open(filename, "w"))
        with open("C:/Users/kalair2/Downloads/table.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                f.writerow([row[0],row[1],row[2],row[3],row[4],row[5]])

        os.remove("C:/Users/kalair2/Downloads/table.csv")

        t = os.listdir("C:/Users/kalair2/Downloads")
        t1 = os.listdir("C:/Python27")
        print t,t1

    
if __name__ == '__main__':
    webcrawl()

    
