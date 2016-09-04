from check_example import my_add, my_mult, my_print
import unittest

class TestMyFunctions(unittest.TestCase):
	def check_add(self):
		self.assertEqual(my_add(2,3), 5)

	def check_mult(self):
		self.assertTrue(my_mult(2,2) == 4)

if __name__ == '__main__':
	unittest.main(exit=False) 
