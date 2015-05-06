import PriceQuery
import csv
import random

pathToTickerList = 'C:\Users\wenzhao\Google Drive\scripts\stockAnalysis\data\CompleteListOfStockTicker\\'
NASQTickerListName = 'NASQList.csv'
NYSETickerListName = 'NYSEList.csv'

SSETickerListName  = 'SSEData.csv'
SZETickerListName  = 'SZEData.csv'

def batchQuery(stockTickerList):
    for stockTicker in stockTickerList:
        PriceQuery.pull_historical_data(stockTicker,'')

def getRandomList(numberNeeded,mode):
    NASQData = csv.reader(open(pathToTickerList+NASQTickerListName,"rb"))
    NYSEData = csv.reader(open(pathToTickerList+NYSETickerListName,"rb"))
    SSEData  = csv.reader(open(pathToTickerList+SSETickerListName,"r"))
    SZEData  = csv.reader(open(pathToTickerList+SZETickerListName,"r"))
    NASQTickers = []
    NYSETickers = []
    SSETickers = []
    SZETickers = []
    AllUSTickers  = []
    AllCNTickers  = []  
    for row in NASQData:
        if row[0].isalpha():
            NASQTickers.append(row[0])
            AllUSTickers.append(row[0])
    for row in NYSEData:
        if row[0].isalpha():
            NYSETickers.append(row[0])
            AllUSTickers.append(row[0])
    for row in SSEData:
        SSETickers.append(row[1]+'.ss')
        AllCNTickers.append(row[1]+'.ss')
    for row in SZEData:
        SZETickers.append(row[1]+'.sz')
        AllCNTickers.append(row[1]+'.sz')
    # mode = 1: only NASQ
    if(mode==1):
        #print(len(NASQTickers))
        return randomSelectN(NASQTickers,numberNeeded)
    # mode = 2 : only NYSE
    elif(mode==2):
        #print(len(NYSETickers))
        return randomSelectN(NYSETickers,numberNeeded)
    # mode = 3 : Both NASQ and NYSE
    elif(mode==3):
        return randomSelectN(AllUSTickers,numberNeeded)
    # mode = 4 : Only Shanghai Exchange
    elif(mode==4):
        return randomSelectN(SSETickers,numberNeeded)
    # mode = 5 : Only Shenzhen Exchange
    elif(mode==5):
        return randomSelectN(SSETickers,numberNeeded)
    # mode = 6: Both Shanghai and Shenzhen
    elif(mode==6):
        return randomSelectN(SSETickers,numberNeeded)
    
def randomSelectN(datalist,n):
    if(n>=len(datalist)):
        return datalist
    else:
        random.shuffle(datalist)
        return datalist[:n]
    
batchQuery(getRandomList(100,6))
#PriceQuery.pull_historical_data('900957.SS','')
#print(getRandomList(100,1))
#print(getRandomList(100,2))        
