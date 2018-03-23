from unittest import TestCase
from uncertainties  import ufloat
from jupyterpc import *

class TestSci(TestCase):
	def test_sci_float(self):
		self.assertEqual(sci(0), '0')
		self.assertEqual(sci(1), '1')
		self.assertEqual(sci(100), '100')
		self.assertEqual(sci(1000), '1000')
		self.assertEqual(sci(1), '1')
	def test_sci_ufloat(self):
		uf = ufloat(100, 20)
		self.assertEqual(sci(uf), uf.format('L'))

class TestTbl(TestCase):
	def test_tbl_list(self):
		self.assertEqual(1,1)

class TestUlist(TestCase):
	def test_ulist_float(self):
		list_val = [1, 1.4325, 1000, 1e-23]
		list_sigma = [0.04, 2000, 23, 1e23]
		self.assertEqual(ulist(list_val, list_sigma), [ufloat(v, s) for v, s in zip(list_val, list_sigma)])
		self.assertEqual(ulist(list_val, 10), [ufloat(v, 10) for v in list_val])


if __name__== '__main__':
	unittest.main()