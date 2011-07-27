import numpy, time, json, urllib

def check():
    data = urllib.urlopen('https://mtgox.com/code/data/ticker.php').read()
    mtgox = json.loads(data)['ticker']
    return (mtgox['low'],mtgox['high'],mtgox['last'])

lasts=[] #list of last prices

def getLast():
    last=check()[2]
    lasts.append(last)

def checkPriceRange(prices):
    rangeText = "["+str(numpy.average(prices)-numpy.std(prices))+"-"+str(numpy.average(prices)+numpy.std(prices))+"]"
    if prices[-1] > numpy.average(prices)+numpy.std(prices): #if last price is greater than average + standard deviation, it's irregularly high
        print "Price increasing", prices[-1], rangeText
    if prices[-1] < numpy.average(prices)-numpy.std(prices): #if last price is lower than average - standard deviation, it's irregularly low
        print "Price decreasing", prices[-1], rangeText
    else:
        print "Price in normal range", prices[-1], rangeText
        
while 1:
    getLast()
    checkPriceRange(lasts[-10:]) #checks last 10 entries
    time.sleep(60)
