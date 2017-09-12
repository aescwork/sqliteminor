# -*- coding: utf-8 -*-

import unittest
import sqlite3
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db


class ReadSearchRowsMultiColumnTest(unittest.TestCase):

	"""
		The read_search_rows method can take either a single value or a list for its target_col and search_val arguments.
		This tests the method by passing lists for these instead of single values.
	"""
	def setUp(self):


		self.conn = setup_db.setup_db()

		self.search_has_any_comp = [(1, u'Ash'), (5, u'Elm'), (6, u'Sugar Maple'), (7, u'Sycamore'), (8, u'Black Cherry'), \
									(10, u'American Chestnut'), (11, u'Elder'), (12, u'Northern Red Oak'), (13, u'Alder Buckthorn'), \
									(14, u'Common Hawthorn'), (15, u'Common Hazel'), (16, u'Midland Hawthorn'), (18, u'Guelder Rose')]

		self.search_has_all_comp = [(8, u'Black Cherry'), (10, u'American Chestnut')]



		self.sm = sqliteminor.SQLiteMinor(self.conn, "trees")
		# Search in the 'name' column for occurrences of both 'che' and 'er' and in the 'qualities' column for occurrences of 'fruit-bearing' and
		#	'deciduous'.  If any of the terms appear in either of their respect columns, the row is retrieved.

		self.has_any = self.sm.read_search_rows(["name","qualities"], [["%che%", "%er%"],["%fruit-bearing%", "%deciduous%"]], "has-any" ,"tree_id, name")
		self.has_any_result = self.sm.result

		# Search in the 'name' column for occurrences of both 'che' and 'er' and in the 'qualities' column for occurrences of 'fruit-bearing' and
		#	'deciduous'.  Only if all of the search terms appear in their respective columns is the row retrieved.

		self.has_all = self.sm.read_search_rows(["name","qualities"], [["%che%", "%er%"],["%fruit-bearing%", "%deciduous%"]], "has-all" ,"tree_id, name")
		self.has_all_result = self.sm.result


	def test_read_search_rows(self):

		self.assertEqual(self.has_any, self.search_has_any_comp)	
		self.assertEqual(self.has_all, self.search_has_all_comp)	


	def test_result(self):

		self.assertEqual(self.has_any_result, "OK")
		self.assertEqual(self.has_all_result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()






