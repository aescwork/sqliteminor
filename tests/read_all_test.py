# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor
import setup_db


class ReadAllTest(unittest.TestCase):

		
	def setUp(self):


		self.comp_read_all_rows = [(1, u'Ash'), (2, u'Yew'), (3, u'White Pine'), (4, u'Scots Pine'), (5, u'Elm'), (6, u'Sugar Maple'), \
									(7, u'Sycamore'), (8, u'Black Cherry'), (9, u'Douglas Fir'), (10, u'American Chestnut'), (11, u'Elder'), \
									(12, u'Northern Red Oak'), (13, u'Alder Buckthorn'), (14, u'Common Hawthorn'), (15, u'Common Hazel'), \
									(16, u'Midland Hawthorn'), (17, u'Redwood (Cupressaceae)'), (18, u'Guelder Rose')]


		conn = setup_db.setup_db()
		self.sm = sqliteminor.SQLiteMinor(conn, "trees")
		self.read_all_rows = [(i[0], i[1]) for i in self.sm.read_all()]

	def test_read_all(self):

		 self.assertEqual(self.comp_read_all_rows, self.read_all_rows)

	def test_result(self):

		self.assertEqual(self.sm.result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()


