import sys
import unittest
sys.path.append("../sqliteminor/")
import sqliteminor as sqm


class InstantiationTest(unittest.TestCase):

	def setUp(self):
		self.sm = sqm.SQLiteMinor("")

	def test_result(self):
		self.assertEqual(self.sm.result, "None")
			

	def test_status(self):
		self.assertEqual(self.sm.status, "None")

	
	def tearDown(self):
		self.sm.__del__()

if __name__ == '__main__':

	unittest.main()
