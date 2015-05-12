

import base64
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from lxml import etree
import urllib

from Stocks.downloadCsv import deleteFile
from compareData import plot2
from downloadCsv import dowload
from plotData import outputList
from plotData import plot1


def home(request):
    
    companyList = readlist()
    
    print companyList
    context = Context({'title':"Company List", 'stocks':companyList,})
    html = get_template('compSelect.html').render(context)
    return HttpResponse(html)

def readlist():
    target = "https://sg.finance.yahoo.com/q/cp?s=^STI"
    f = urllib.urlopen(target)
    page = f.read().decode("utf-8")
    f.close()
    results = []
    tree = etree.HTML(page)
    for n in tree.xpath("//tr"):
         group = n.xpath("./td[@class='yfnc_tabledata1']")
         if len(group) > 1:
             results.append((group[0][0][0].text, group[1].text))
    return(results)

def getCurrentStock(comp):
    target = "https://sg.finance.yahoo.com/q/cp?s="+comp
    f = urllib.urlopen(target)
    page = f.read().decode("utf-8")
    f.close()
    results = []
    tree = etree.HTML(page)
    compName = tree.xpath("//div[@class='title']/h2/text()")
    val = tree.xpath("//span[@class='time_rtq_ticker']/text()")
    lower = tree.xpath("//span[@class='down_r time_rtq_content']/text()")
    upper = tree.xpath("//span[@class='up_g time_rtq_content']/text()")
    results.append(compName[0])
    results.append(val[0])
    if len(lower)!=0:
        results.append(lower[0])
        results.append("images/down.png")
    elif len(upper)!=0:
        results.append(upper[0])
        results.append("images/up.png")
    return results
def pageSubmit(request,comp,type):
    currentData = getCurrentStock(comp)
    filePath = dowload(comp)
    dataList=outputList(filePath)
    imageUri = plot1(filePath,currentData[0],type)
    deleteFile(filePath)
    context = Context({'title':"Company List", 'imageUri':imageUri,'dataList':dataList,'stock1':currentData,'type':type})
    html = get_template('graph.html').render(context)
    return HttpResponse(html)
    
def compare (request):
    companyList = readlist()
    context = Context({'title':"Company List", 'stocks':companyList})
    html = get_template('compCompare.html').render(context)
    return HttpResponse(html)

def compareSubmit(request,comp1,comp2,type):
    filePath1 = dowload(comp1)
    filePath2 = dowload(comp2)
    stock1 = getCurrentStock(comp1)
    stock2 = getCurrentStock(comp2)
    imageUri = plot2(filePath1,filePath2,stock1[0],stock2[0],type)
    dataList = outputList(filePath1)
    dataList1 =outputList(filePath2)
    deleteFile(filePath1)
    deleteFile(filePath2)
    context = Context({'title':"Company List", 'imageUri':imageUri,'dataList':dataList,'dataList1':dataList1,"stock1":stock1,"stock2":stock2,"type":type})
    html = get_template('graph.html').render(context)
    return HttpResponse(html)
    
   
    