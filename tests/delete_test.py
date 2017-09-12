# -*- coding: utf-8 -*-

import unittest
import sqlite3 
import sys
sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db


class DeleteTest(unittest.TestCase):
		
	def setUp(self):


		self.has_any_remainder_comp = [(2, u'Yew'), (3, u'White Pine'), (4, u'Scots Pine'), (9, u'Douglas Fir'), (17, u'Redwood (Cupressaceae)')]

		self.has_all_remainder_comp = [(1, u'Ash'), (2, u'Yew'), (3, u'White Pine'), (4, u'Scots Pine'), (5, u'Elm'), (6, u'Sugar Maple'), \
										(7, u'Sycamore'), (9, u'Douglas Fir'), (11, u'Elder'), (12, u'Northern Red Oak'), (13, u'Alder Buckthorn'), \
										(14, u'Common Hawthorn'), (15, u'Common Hazel'), (16, u'Midland Hawthorn'), (17, u'Redwood (Cupressaceae)'), \
										(18, u'Guelder Rose')]

		self.has_all_rows_deleted_comp = 2
		self.has_any_rows_deleted_comp = 13

		"""
			Test the delete() method with two possibilities.  ...
		"""

		self.sm = sqliteminor.SQLiteMinor(setup_db.setup_db(), "trees")
		self.has_any_rows_deleted = self.sm.delete(["name","qualities"], [["%che%", "%er%"],["%fruit-bearing%", "%deciduous%"]], "has-any")
		self.has_any_result = self.sm.result

		self.sm.cursor.execute("SELECT tree_id, name FROM trees")
		self.has_any_remainder = self.sm.cursor.fetchall()

		del(self.sm)

		self.sm = sqliteminor.SQLiteMinor(setup_db.setup_db(), "trees")
		self.has_all_rows_deleted = self.sm.delete(["name","qualities"], [["%che%", "%er%"],["%fruit-bearing%", "%deciduous%"]], "has-all")
		self.has_all_result = self.sm.result

		self.sm.cursor.execute("SELECT tree_id, name FROM trees")
		self.has_all_remainder = self.sm.cursor.fetchall()


	def test_delete(self):

		"""
			Compare the rows left in the table after each sm.delete() calls with test values.
		"""

		self.assertEqual(self.has_all_remainder_comp, self.has_all_remainder)	
		self.assertEqual(self.has_any_remainder_comp, self.has_any_remainder)	

		self.assertEqual(self.has_all_rows_deleted_comp, self.has_all_rows_deleted)	
		self.assertEqual(self.has_any_rows_deleted_comp, self.has_any_rows_deleted)	


	def test_result(self):

		"""
			Compare the results of each sm.delete() call with test values.
		"""

		self.assertEqual(self.has_all_result, "OK")
		self.assertEqual(self.has_any_result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()






