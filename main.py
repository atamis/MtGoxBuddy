import numpy, time, json, urllib, sys
def check():
    data = json.loads(urllib.urlopen('https://mtgox.com/code/data/ticker.php').read())['ticker']
    return (data['low'],data['high'],data['last'])
lasts=[] #list of last prices
def checkPriceRange(prices):
    rangeText = "["+str(numpy.average(prices)-numpy.std(prices))+"-"+str(numpy.average(prices)+numpy.std(prices))+"]"
    if prices[-1] > numpy.average(prices)+numpy.std(prices):print "Price increasing", prices[-1], rangeText #if last price is greater than average + standard deviation, it's irregularly high
    if prices[-1] < numpy.average(prices)-numpy.std(prices):print "Price decreasing", prices[-1], rangeText #if last price is lower than average - standard deviation, it's irregularly low
    else: print "Price in normal range", prices[-1], rangeText
while 1: last=check()[2]; lasts.append(last);checkPriceRange(lasts[-10:]);time.sleep(float(sys.argv[1]) if len(sys.argv) > 1 else 60)
