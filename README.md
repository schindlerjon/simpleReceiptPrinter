simpleReceiptPrinter
====================
This program simply makes a simple receipt from an indicated text file.


Input/Output
------------
Input: 
Text file containing a list of items to be purchased.

Output: 
A receipt/list of all the purchased items with taxes added.



How to Run
-----------
The user must enter the desired file's name on the command line initially to run the program as so:

       cmd>> python simpleReceiptPrinter.py filename.txt
       
This will ensure that the proper file is read from. 
Each file must be formmatted in a specific manner, as follows:

      # item_count "description" as price
      
      Example.txt
      -----------
      1 imported bottle of French wine at 25.99
      1 imported jar of pickles at 3.99
      5 Quantum Algorithms books at 15.97
      1 unknown domestic item at 8.88



Program Details/Assumptions
---------------------------
How Taxes Work
Taxes in this program are computed based on the description of the item. 
If the item is a book, involved in the mdeical field, or any foodstuff, it 
is exempt from sales tax. If the item has been imported, then an Import tax
is placed on the item, regardless on if it meets the requirements for 
exemption or not. So one item may have both the sales tax and import tax.
The sales tax is 10% and the import tax is 5%. The tax is then rounded up to 
the nearest $0.05, so $0.31 would round to $0.35, while $0.55 would remain.
In this program the definitions for "Exempt" and "Imported" are as follows:

"Exempt" Definition
Those items that are found as exempt must contain at least one of these words:

    "book", "books", "food", "chocolate", "chocolates", "bread", "medical", "pills"

"Imported" Definition
Those items that are found as imported must contain at least one of these words:

    "import", "imported", "from", "\'merica", "krypton", "gallifrey"
    
Additionally, taxes are applied for one object, then multiplied by the number of 
objects that have been purchased. 

We assume that the user would never use any descriptive words to describe 
non-imported objects. We also assume that the user will only use the words
described within the "exempt" section to describe those items that are exempt.
This can easily be expanded though to include more items. 



Further Works
-------------
This simple program can be expanded to use a Naive Bayes classifier on the object
description to decide whether an item is imported or whether it should be exempt
from the basic sales tax. 








