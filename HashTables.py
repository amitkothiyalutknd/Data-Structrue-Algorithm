stockPriceList = []
with open("F:/Python_Study/DSA/StockPrice.csv", "r") as file:
    for line in file:
        day, price = line.split(',')
        price = float(price)
        stockPriceList.append([day, price])
    print("Representation of List(Retrieve From CSV File):\n", stockPriceList)
    date = '02-Mar'
    for element in stockPriceList:
        if element[0] ==  date:
            print(f"The Price on {date} is(Retrieve From CSV File) using List:\t", element[1])

stockPriceListDict = {}
with open("F:/Python_Study/DSA/StockPrice.csv", "r") as file:
    for line in file:
        day, price = line.split(',')
        price = float(price)
        stockPriceListDict[day] = price
    print('\nRepresentation of List Via Dictionary(Retrieve From CSV File):\n', stockPriceListDict)
    print("The Price on date->2-March is(Retrieve From CSV File) using Dictinory:\t", stockPriceListDict['02-Mar'])

print("\nShowing ASCII Value of Character B:\t", ord('B'))

def gethash(key):
    sum = 0
    for chr in key:
        sum += ord(chr)
    return sum % 100
print("\nShowing Hash Integer Values of date '02-March' in HashTableMemory:\t", gethash('02-mar'))

class HashTable:                    #Implementation Hash Table.
    def __init__(self):
        self.Max = 100
        self.arr = [None]*self.Max

    def gethash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr)
        return sum % 100

    def __setitem__(self, key, val):
        h = self.gethash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.gethash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.gethash(key)
        print(f"\nDeleting Element Using {h}")
        self.arr[h] = None

h1 = HashTable()    
h1['02-mar'] = 786
h1['11-apr'] = 596
h1['31-may'] = 427
h1['09-jun'] = 653
h1['18-jul'] = 852
print("\n<-----------------------------Visulization HashTable Implementation----------------------------->")
print("\nShowing Price Value of Key Date '2-March' is:\t", h1['02-mar'])
print("Showing HashTable Array & Its Values:\n", h1.arr)
del h1['02-mar']
print("\nShowing Price Value of Key date '2-March' after Deletion Operation Applied:\t", h1['02-mar'])
print("Showing HashTable Array & Its Values after Deletion Operation Applied:\n", h1.arr)


class HashTablesC:                  #Implementation Hash Table To Avoid Collision Using Chaining Method.
    def __init__(self):
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]

    def gethash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr)
        return sum % 100

    def __setitem__(self, key, val):
        h = self.gethash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.gethash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        arridx = self.gethash(key)
        for idx, kv in enumerate(self.arr[arridx]):
            if kv[0] == key:
                print(f"Deleting Element Using {arridx} & {idx}")
                del self.arr[arridx][idx]
        
h2 = HashTablesC()
print("\nPrinting Hash Value of 'march 6':\t", h2.gethash('march 6'))
print("Printing Hash Value of 'march 17':\t", h2.gethash('march 17'))
h2['02-mar'] = 786
h2['11-apr'] = 596
h2['31-may'] = 427
h2['09-jun'] = 653
h2['18-jul'] = 852
print("<-----------------------------Visulization HashTable Implementation Avoiding Collision Using Chaining Method----------------------------->")
print("\nShowing Price Value of Key Date '9-jun' is:\t", h2['09-jun'])
print("Showing HashTable Array & Its Values Before Deletion Operation Applied:\n", h2.arr)
del h2['09-jun']
print("Showing HashTable Array & Its Values after Deletion Operation Applied:\n", h2.arr)