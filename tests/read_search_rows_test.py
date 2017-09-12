# -*- coding: utf-8 -*-

import unittest
import sqlite3
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db


class ReadSearchRowsTest(unittest.TestCase):

	def setUp(self):


		self.conn = setup_db.setup_db()

		self.search_term_at_end_comp = [(11, u'Elder')]

		self.search_term_at_beginning_comp = [(5, u'Elm'), (11, u'Elder')]

		self.search_term_anywhere_comp = [(5, u'Elm'), (11, u'Elder'), (15, u'Common Hazel'), (18, u'Guelder Rose')]


		self.sm = sqliteminor.SQLiteMinor(self.conn, "trees")
		# Search through the name column of each row for the string 'er' occurring only at the end of a name
		self.search_term_at_end = self.sm.read_search_rows("name", "%er", "has-any" ,"tree_id, name")
		self.search_term_at_end_result = self.sm.result
		# Search through the name column of each row for the string 'el' occurring only at the beginning of a name
		self.search_term_at_beginning = self.sm.read_search_rows("name", "el%", "has-any" ,"tree_id, name")
		self.search_term_at_beginning_result = self.sm.result
		# Search through the name column of each row for the string 'el' occurring anywhere in a name
		self.search_term_anywhere = self.sm.read_search_rows("name", "%el%", "has-any" ,"tree_id, name")
		self.search_term_anywhere_result = self.sm.result


	def test_read_search_rows(self):

		self.assertEqual(self.search_term_at_end, self.search_term_at_end_comp)	
		self.assertEqual(self.search_term_at_beginning, self.search_term_at_beginning_comp)	
		self.assertEqual(self.search_term_anywhere, self.search_term_anywhere_comp)


	def test_result(self):

		self.assertEqual(self.search_term_at_end_result, "OK")
		self.assertEqual(self.search_term_at_beginning_result, "OK")
		self.assertEqual(self.search_term_anywhere_result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()






