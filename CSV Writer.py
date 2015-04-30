import csv

def writeDataFile(csvDict, csvFileName, fieldNames):
    print csvDict, fieldNames
    with open('%s.csv' % csvFileName, 'wb') as outfile:
        writer = csv.DictWriter(outfile, fieldnames = fieldNames)
        writer.writeheader()
        print 'header written'
        rowList = []
        for i in range(len(csvDict[fieldNames[0]])):
            rowDict = {}
            for key in csvDict.keys():
                rowDict[key] = csvDict[key][i]
            rowList.append(rowDict)
        #blah = [k for k in rowdict if k not in fieldnames]
        writer.writerows(rowList)
        
csvDictionary = {'list': [1,2,3], 'list2': ['a','b','c']}
writeDataFile(csvDictionary, 'csvFile', ['list2', 'list'])