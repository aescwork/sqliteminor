# -*- coding: utf-8 -*-

import unittest
import sqlite3
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db




class UpdateTest(unittest.TestCase):

	"""
		Test the update() method by updating the rows twice -- first by changing the qualities column of qualifying rows based on 
		the content already in the qualities column, second by changing the qualities column of qualifying rows based on if a search
		term is present in the name column.  Verify the resulting rows which should have been updated.  Verify also the number of
		rows modified in each test.
	"""

	def setUp(self):

		self.first_update_comp = [(2, u'Yew', u'coniferous'), (3, u'White Pine', u'coniferous'), (4, u'Scots Pine', u'coniferous'), \
									(9, u'Douglas Fir', u'coniferous'), (17, u'Redwood (Cupressaceae)', u'coniferous')]
	
		self.second_update_comp = [(13, u'Alder Buckthorn', u'seasonal'), (14, u'Common Hawthorn', u'seasonal'), \
									(16, u'Midland Hawthorn', u'seasonal')]

		self.first_update_n_rows_comp = 5

		self.second_update_n_rows_comp = 3 
		
		self.sm = sqliteminor.SQLiteMinor(setup_db.setup_db(), "trees")

		# update all rows which have 'evergreen' in their qualities column to have only 'coniferous' in their qualities column

		self.first_update_n_rows = self.sm.update("qualities", "coniferous", "qualities", "evergreen%")	
		self.first_update_result = self.sm.result

		self.sm.cursor.execute("SELECT tree_id, name, qualities FROM trees WHERE qualities LIKE 'coniferous'")
		self.first_update = self.sm.cursor.fetchall()

		# update all rows which have the term 'thorn' somewhere in their name to have only 'seasonal' in their qualities column
		self.second_update_n_rows = self.sm.update("qualities", "seasonal", "name", "%thorn%")
		self.second_update_result = self.sm.result

		self.sm.cursor.execute("SELECT tree_id, name, qualities FROM trees WHERE name LIKE '%thorn%'")
		self.second_update = self.sm.cursor.fetchall()


	def test_update(self):
		self.assertEqual(self.first_update_n_rows_comp, self.first_update_n_rows)	
		self.assertEqual(self.second_update_n_rows_comp, self.second_update_n_rows)	

		self.assertEqual(self.first_update, self.first_update_comp)
		self.assertEqual(self.second_update, self.second_update_comp)

	def test_result(self):
		self.assertEqual(self.first_update_result, "OK")
		self.assertEqual(self.second_update_result, "OK")


	def tearDown(self):

		self.sm.__del__()

if __name__ == '__main__':
	unittest.main()



