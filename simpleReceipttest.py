import unittest
import simpleReceiptPrinter

class TestSimpleReceiptPrinter(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_getItem(self):
		test_list = ["1","lotion","on","the","skin","at","7","13"]
		results   = ( 1 ,["lotion","on","the","skin"], 7.13 )
		self.assertEqual( simpleReceiptPrinter.getItem(test_list), results )	
		
	def test_isImported(self):
		temp = ["imported", "bottle", "of", "chartruse"]
		self.assertEqual( simpleReceiptPrinter.isImported(temp), True)

	def test_isExempt(self):
		temp = ["engineering", "ethics", "book"]
		self.assertEqual( simpleReceiptPrinter.isSalesExempt(temp), True)	
		
	def test_isNotExempt(self):
		temp = ["Justin", "Beiber", "CD"]
		self.assertEqual( simpleReceiptPrinter.isImported(temp), False)

	def test_RoundSalesTax(self):
		self.assertEqual( simpleReceiptPrinter.roundSalesTax(3.01), 3.05)
	
	def test_RoundSalesTax2(self):
		self.assertEqual( simpleReceiptPrinter.roundSalesTax(7.35), 7.35)
		
if __name__ == '__main__':
    unittest.main()




