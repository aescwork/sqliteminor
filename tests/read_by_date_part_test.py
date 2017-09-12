# -*- coding: utf-8 -*-

import unittest
import sqlite3
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db
import datetime

class ReadByDatePartTest(unittest.TestCase):

	"""
		test the read_by_date_part() method.  Retrieves one or more rows from an sqlite database depending on whether the row has a 
		passed-in year,month or day in a column containing dates whose column data type is DATE.
	"""
	def setUp(self):
		

		self.search_by_month_comp = [(u'Alder Buckthorn', datetime.date(2017, 4, 14)), (u'Black Cherry', datetime.date(2017, 4, 9)), \
										(u'Sugar Maple', datetime.date(2017, 4, 25)), (u'Sycamore', datetime.date(2017, 4, 10))]

		self.search_by_day_comp = [(u'Common Hawthorn', datetime.date(2017, 2, 11)), (u'Elder', datetime.date(2017, 2, 11)), \
									(u'Elm', datetime.date(2017, 2, 11)), (u'Guelder Rose', datetime.date(2017, 2, 11)), \
									(u'Midland Hawthorn', datetime.date(2017, 2, 11)), (u'Northern Red Oak', datetime.date(2017, 2, 11)), \
									(u'Redwood (Cupressaceae)', datetime.date(2017, 2, 11)), (u'Scots Pine', datetime.date(2017, 2, 11))]


		conn = setup_db.setup_db()
		self.sm = sqliteminor.SQLiteMinor(setup_db.setup_db(), "trees")
		self.search_by_month = self.sm.read_by_date_part("month", "sample_date", "04", "name, sample_date")
		self.search_by_month_result = self.sm.result
		self.search_by_day = self.sm.read_by_date_part("day", "sample_date", "11", "name, sample_date")
		self.search_by_day_result = self.sm.result

		
		
	def test_some_method(self):

		self.assertEqual(self.search_by_month, self.search_by_month_comp)	
		self.assertEqual(self.search_by_day, self.search_by_day_comp)	

	def test_result(self):
		self.assertEqual(self.search_by_month_result, "OK")
		self.assertEqual(self.search_by_month_result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()








