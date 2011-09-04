"""The stockTunes program

This is a script that will act as StockManager
"""

__author__ =  'Eli Katz'
__version__=  '1.0'

import ystockquote

class StockManager():
    """StockManager is an encapsulation for the ystockquote library
    """
    stockList = []
    
    def __init__(self):
        """
        Constructor opens the stock cfg file and reads in the stocks to a list
        """
        f = open('stocks.cfg', 'r')
        for line in f:
            if (self.isValid(line.rstrip())):
                self.stockList.append(line.rstrip())
            
    def getChange(self):
        """Returns the net change in stocks for the group of stocks looked at"""
        sum = 0;
        for item in self.stockList:
            sum += float(ystockquote.get_change(item)) 
        print sum
        return True
        
    def isValid(self, stock):
        """Checks whether a stock symbol is valid"""
        if (ystockquote.get_change(stock) == 'N/A'):
            return False
        else:
            return True