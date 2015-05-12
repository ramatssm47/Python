import urllib2
import os
#plotData.plot1()
def dowload(name):
    url = 'http://ichart.yahoo.com/table.csv?s='+name

    u = urllib2.urlopen(url)
    localFile = open(name+'.csv', 'w')
    localFile.write(u.read())
    localFile.close()
    print "download Over"+name+'.csv'
    return localFile.name

def deleteFile(name):
    
    os.remove(name)