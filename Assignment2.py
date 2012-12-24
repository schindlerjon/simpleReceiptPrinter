
# PROBLEM TWO: SALES TAXES
 
# Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. 
# Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.
 
# When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), 
# finishing with the total cost of the items, and the total amounts of sales taxes paid.  
# The rounding rules for sales tax are that for a tax rate of n%, 
# a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.
 
# Write an application that prints out the receipt details for these shopping baskets...
# INPUT:
 
# Input 1:
# 1 book at 12.49
# 1 music CD at 14.99
# 1 chocolate bar at 0.85
 
# Input 2:
# 1 imported box of chocolates at 10.00
# 1 imported bottle of perfume at 47.50
 
# Input 3:
# 1 imported bottle of perfume at 27.99
# 1 bottle of perfume at 18.99
# 1 packet of headache pills at 9.75
# 1 box of imported chocolates at 11.25
 
# OUTPUT
 
# Output 1:
# 1 book : 12.49
# 1 music CD: 16.49
# 1 chocolate bar: 0.85
# Sales Taxes: 1.50
# Total: 29.83
 
# Output 2:
# 1 imported box of chocolates: 10.50
# 1 imported bottle of perfume: 54.65
# Sales Taxes: 7.65
# Total: 65.15
 
# Output 3:
# 1 imported bottle of perfume: 32.19
# 1 bottle of perfume: 20.89
# 1 packet of headache pills: 9.75
# 1 imported box of chocolates: 11.85
# Sales Taxes: 6.70
# Total: 74.68
# ==========

import pprint
import re

pp = pprint.PrettyPrinter(depth=6)

WORDS_IMPORT = ["import", "imported", "from", "\'merica", "krypton", "gallifrey"]
WORDS_EXEMPT = ["book", "books", "food", "chocolate", "chocolates", "bread", "medical", "pills"]
# "Bread makes you fat?!" - Scott Pilgrim vs the World


def tokenize(text):
	return re.findall("\w+", text.lower())

# Assume that each price is entered as "x.xx"
def getItem(list):
	count  = int(list[0])
	#print count
	del(list[0])
	cents   = float(list[len(list)-1])
	del(list[len(list)-1])
	dollars = float(list[len(list)-1])
	del(list[len(list)-1])
	del(list[len(list)-1])
	itemPrice = dollars + cents/100
	return count, list, itemPrice
	
def printReceipt(listItems):
	#print listItems

	imported = False;
	exempt = False;
	sales_tax  = 0;
	total_tax  = 0;
	total_cost = 0;
	
	print "Receipt:\n-------"
	for item in listItems:
		imported = False;
		exempt = False;
		sales_tax = 0;
		
		# print item[0]," ".join(item[1]),"%.2f"%item[2]
		# Decide if Item is a book, food, or medical product
		print isImported(item[1]), isSalesExempt(item[1])
		
		if(isImported(item[1])):
			sales_tax = item[2] * 0.05
		
		if(not isSalesExempt(item[1])):
			sales_tax = item[2] * 0.10

		
		print import_tax, sales_tax, item[2]
		print item[0], " ".join(item[1]), item[2]+ sales_tax
		# Decide if the item is an import
		
		total_tax  += sales_tax 
		total_cost += float(item[2])
	print "Sales Tax: ", "%.2f"%total_tax
	print "Total: ", "%.2f"%(total_cost + total_tax)
	print "==========="
	
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

if __name__=="__main__":
	print "****************\n  ASSIGNMENT 2\n****************"
	
	# Read in from File
	text1 = "1 imported of chocolates at 10.00"
	text2 = "1 imported bottle of perfume at 47.50"
	#text1 = "1 book at 12.49"
	#text2 = "1 music CD at 14.99"
	#text3 = "1 chocolate bar at 0.85"
	
	# form a List of items within the file
	listItems = []
	listItems.append(text1)
	listItems.append(text2)
	#listItems.append(text3)
	
	# Configure the List to Calculate
	listItems = tokenizeList(listItems)
	
	# Print the final Receipt
	printReceipt(listItems)