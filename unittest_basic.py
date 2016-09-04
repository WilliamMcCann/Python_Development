from check_example import my_add, my_mult, my_print
import unittest

class TestMyFunctions(unittest.TestCase):
	def test_contains_simple_true(self):
		self.assertEqual(my_add(2, 3), 5)

	def test_first_numbers(self):
		self.assertEqual(my_mult(2,2), 4)

if __name__ == '__main__':
	unittest.main(exit=False)
