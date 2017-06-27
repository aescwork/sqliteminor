# -*- coding: utf-8 -*-

import unittest
import sys
import os
import sqlite3 
sys.path.append("../sqliteminor/")
import sqliteminor 


class AddTest(unittest.TestCase):

	def setUp(self):
		self.path_to_db = "../fixtures/sqlm_test.db"
		table_name = "trees"
		self.conn = sqlite3.connect(self.path_to_db)
		self.curs = self.conn.cursor()
		self.curs.execute("CREATE TABLE trees(tree_id INT, name TEXT, age INT)")
		self.sm = sqliteminor.SQLiteMinor(self.conn, table_name)
		self.tree_entry = (1, "ash", 100)
		self.sm.add(self.tree_entry)
		self.curs.execute("SELECT * FROM trees")
		self.cols = self.curs.fetchone()
		

	def test_add(self):
	
		for t, c in zip(self.tree_entry, self.cols):
			self.assertEqual(t, c)	


	def test_result(self):

		self.assertEqual(self.sm.result, "OK")


	def tearDown(self):

		self.sm.__del__()
		os.remove(self.path_to_db)

if __name__ == '__main__':
	unittest.main()
