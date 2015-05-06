import sys
import csv
type = sys.getfilesystemencoding()

pathToTickerList = 'G:\stockAnalysis\data\CompleteListOfStockTicker\\'
SSERawDataName = 'SSE_raw_list.txt'
SZERawDataName = 'SZE_raw_list.txt'

SSEDict = {}
SZEDict = {}

SSERawData = open(pathToTickerList+SSERawDataName,'r')
SZERawData = open(pathToTickerList+SZERawDataName,'r')

SSEData = SSERawData.read()
#print(SSEData)
SZEData = SZERawData.read()
#print(SZEData)
flag =0
tempKey=''
tempValue=''
for char in SSEData:
    if(char==' '):
        continue
    elif(char=='('):
        flag = 1
    elif(char==')'):
        flag = 0
        SSEDict[tempKey]=tempValue
        tempKey=''
        tempValue=''
    else:
        if(flag==0):
            tempKey+=char
        else:
            tempValue+=char
#print(SSEDict)
w = csv.writer(open(pathToTickerList+"SSEData.csv", "w"))
for key, val in SSEDict.items():
    w.writerow([key, val])
            
for char in SZEData:
    if(char==' '):
        continue
    elif(char=='('):
        flag = 1
    elif(char==')'):
        flag = 0
        SZEDict[tempKey]=tempValue
        tempKey=''
        tempValue=''
    else:
        if(flag==0):
            tempKey+=char
        else:
            tempValue+=char
#print(SZEDict)
w = csv.writer(open(pathToTickerList+"SZEData.csv", "w"))
for key, val in SZEDict.items():
    w.writerow([key, val])
