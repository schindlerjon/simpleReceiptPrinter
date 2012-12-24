import pprint
import string
import sys
import re

pp = pprint.PrettyPrinter(depth=6)

FILENAME = sys.argv[-1]
WORDS_IMPORT = ["import", "imported", "from", "\'merica", "krypton", "gallifrey"]
WORDS_EXEMPT = ["book", "books", "food", "chocolate", "chocolates", "bread", "medical", "pills"]
# "Bread makes you fat?!" - Scott Pilgrim vs the World


def tokenize(text):
	return re.findall("\w+", text.lower())

def getItem(list):
	# list = "count detail detail at $.$$"
	count  = int(list[0])
	del(list[0])		   		# Get rid of count
	cents   = float(list[len(list)-1])
	del(list[len(list)-1]) 		# Get rid of cents
	dollars = float(list[len(list)-1])
	del(list[len(list)-1]) 		# Get rid of dollars
	del(list[len(list)-1]) 		# Get rid of "at"
	itemPrice = dollars + cents/100
	return count, list, itemPrice
	
def printReceipt(listItems):
	total_tax  = 0
	total_cost = 0
	
	print "Receipt:\n-------"
	for item in listItems:
		sales_tax = 0	# Resets to 0 everytime
		
		# Decide if the item is Imported
		if(isImported(item[1])):
			sales_tax += item[2] * 0.05
		
		# Decide if Item is a book, food, or medical product
		if(not isSalesExempt(item[1])):
			sales_tax += item[2] * 0.10

		# Round the sales tax to the nearest $0.05
		sales_tax = roundSalesTax(sales_tax)
		total_tax  += item[0] * sales_tax 		# Add Sales Tax to the total tax
		total_cost += item[0] * float(item[2])			# Add the costs together
		
		print item[0], " ".join(item[1]), "%.2f"%(item[0]*(item[2]+ sales_tax))
	print "Sales Tax: ", "%.2f"%total_tax
	print "Total: ", "%.2f"%(total_cost + total_tax)
	print "==========="
	
def roundSalesTax(tax):
	return round((tax+0.0249)*20)/20
	
	

def isImported(itemDetail):
	for word in itemDetail:
		for desc in WORDS_IMPORT:
			if(word.lower() == desc.lower()):
				return True
			
	return False
	
def isSalesExempt(itemDetail):
	for word in itemDetail:
		for desc in WORDS_EXEMPT:
			if(word.lower() == desc.lower()):
				return True
			
	return False

def tokenizeList(list):
	tokenList = []
	for itemString in list:
		tokenList.append(getItem(tokenize(itemString)))
	return tokenList

def readFile(filename):
	fileList = []
	f = open(filename)
	while 1:
		line = f.readline()
		if not line:
			break
		fileList.append(line)
	
	f.close()
	return fileList
	
if __name__=="__main__":
	listItems = []
	
	# Read in from File
	listItems = readFile(FILENAME)
	
	# Configure the List to Calculate
	listItems = tokenizeList(listItems)
	
	# Print the final Receipt
	printReceipt(listItems)