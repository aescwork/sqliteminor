# -*- coding: utf-8 -*-

import unittest
import os
import sys
import sqlite3
import datetime

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db

class ReadRangeTest(unittest.TestCase):

	def setUp(self):

		self.comp_name_range = [(4, u'Scots Pine'), (5, u'Elm'), (8, u'Black Cherry'), (9, u'Douglas Fir'), (11, u'Elder'), \
								(12, u'Northern Red Oak'), (14, u'Common Hawthorn'), (15, u'Common Hazel'), (16, u'Midland Hawthorn'),\
								 (17, u'Redwood (Cupressaceae)'), (18, u'Guelder Rose')]

		self.comp_sample_date_range = [(datetime.date(2017, 3, 10), u'American Chestnut'), (datetime.date(2017, 3, 20), u'Douglas Fir'), \
										(datetime.date(2017, 4, 9), u'Black Cherry'), (datetime.date(2017, 4, 10), u'Sycamore'), \
										(datetime.date(2017, 4, 14), u'Alder Buckthorn'), (datetime.date(2017, 4, 25), u'Sugar Maple'), \
										(datetime.date(2017, 5, 2), u'Common Hazel'), (datetime.date(2017, 5, 5), u'White Pine'), \
										(datetime.date(2017, 5, 10), u'Yew')]


		self.comp_tree_id_range = [(3, u'White Pine'), (4, u'Scots Pine'), (5, u'Elm'), (6, u'Sugar Maple'), (7, u'Sycamore'), \
									(8, u'Black Cherry'), (9, u'Douglas Fir')] 

		self.comp_age_range = [(100, u'Elm'), (120, u'Scots Pine'), (120, u'Sugar Maple'), (150, u'American Chestnut'), \
								(200, u'Ash'), (240, u'Northern Red Oak'), (500, u'Douglas Fir')]

		self.conn = setup_db.setup_db()
		self.sm = sqliteminor.SQLiteMinor(self.conn, "trees")

		self.name_range = self.sm.read_range("Black", "Sugar", "name", "tree_id, name")
		self.name_range_result = self.sm.result

		self.sample_date_range = self.sm.read_range('2017-03-10', '2017-05-10', "sample_date", "sample_date, name")
		self.name_date_range_result = self.sm.result

		self.tree_id_range = self.sm.read_range(3, 9, "tree_id", "tree_id, name")
		self.name_tree_id_range_result = self.sm.result

		self.age_range = self.sm.read_range(100, 500, "age", "age, name")
		self.name_age_range_result = self.sm.result


	def test_read_range(self):
		self.assertEqual(self.name_range, self.comp_name_range)	
		self.assertEqual(self.sample_date_range, self.comp_sample_date_range)	
		self.assertEqual(self.tree_id_range, self.comp_tree_id_range)	
		self.assertEqual(self.age_range, self.comp_age_range)	
			


	def test_result(self):
		self.assertEqual(self.name_range_result, "OK")
		self.assertEqual(self.name_date_range_result, "OK")
		self.assertEqual(self.name_tree_id_range_result, "OK")
		self.assertEqual(self.name_age_range_result, "OK")


	def tearDown(self):

		self.sm.__del__()
		del(self.conn)

if __name__ == '__main__':
	unittest.main()







