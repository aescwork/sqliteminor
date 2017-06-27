"""

..	currentmodule:: sqliteminor
	:platform: Unix, Windows
	:synopsis:  simple class template

.. moduleauthor:: Vollund Leysing  aescwork@protonmail.com


"""

import sys

# import sqlite3 as lite	maybe don't need this import since everything will be done with the conn created outside the class

class SQLiteMinor(object):


	def __init__(self, conn=None, table=None):

		"""

		Args: 
			db_file_path (str):			The path to the database file with which this object will be working.
			conn (Sqlite3.Connection):	A connection object for interfacing with an sqlite database.
		"""
		self.result = "None"
		self.status = "None"
		self.order = "forward"	# must be either 'forward' (entries returned first to last) or 'backward' (entries returned last to first)
		self.table = table
		self._conn = conn # create the connection outside of this class ... like with an object of the sqlitemgr class (see README.txt).
		self.statement = ""
		self._cursor = None

		self._create_cursor()

	def __del__(self):
		"""
			Just close the connection when deleted.
		"""
		if self._conn:
			self._conn.close()


	@property
	def conn(self):
		""" 
		Get the conn (call it directly: obj.cursor)
		"""
		return self._conn

	
	@conn.setter
	def conn(self, val):
		self._conn = val
		self._create_cursor()


	def add(self, members, table=None):
		"""
		Add (create) a row in the table whose name is assigned to self.table.

		Args:
				members (tuple):	A tuple with the values to be inserted in the database.  The values must be from left to right (first to last)
									in the order in which columns of the target table were created.  

									For example if a table was created with a statement like:

												CREATE TABLE trees(Id INT, tree_name TEXT, age_in_years INT)

									and a row is to be inserted for a tree with an Id of 1, a tree_name of "ash", and age_in_years of 200 then the values 
									in the members tuple must also be in this order: (1, "ash", 200).



				table (str):		The name of the table to which the row is to be added.


		.. warning::
									This method can only execute one INSERT at a time.

			"""

		if table:
			self.table = table

		try:
			placeholders = "("
			c = 1
			for m in members:						
				if c == len(members): 
					placeholders = placeholders + "?)"
				else:
					placeholders = placeholders + "?, "
				c = c + 1

			self.statement = "INSERT INTO " + self.table + " VALUES" + placeholders
			self._cursor.execute(self.statement, members)
			self.conn.commit()
			self._set_result_and_status("OK", "")
		
		except Exception as e:
			msg = "In SqliteMinor add(): ", str(e)
			self._set_result_and_status("FAIL", msg)
		
	

	def read_range(self, frm, to):
		"""
		self._set_result_and_status( , )
		"""


	def read_head(self, number):
		return True


	def read_tail(self, number):
		return True



	def read_rows(self, column_id, search_val):
		return True



	def read_search(self, column_id, search_val):
		return True



	def read_single_field(self, ref_column_id, ref_column_val, target_column_id):
		return True


	
	def read_alt_table_referant(self, alt_table, search_vals):
		"""
		Args:
			search_vals (self, list):	
		"""
		return True



	def update(self, ref_column_id, ref_column_val, target_column, updated_val):
		return True

		

	def delete(self, ref_column_id, ref_val):
		return True




	def _set_result_and_status(self, result, status):
		"""
		Set self.result and self.status here to help DRY out the code in the above methods.
		
		Args:
			result (self, string):	the result of the operation performed by the calling method.
			status (self, string):	the status (self, description) of the outcome of the operation performed by the calling method.
		"""
		self.result = result
		self.status = status


	def _check_order(self):
		"""
			Make sure order is either 'forward' or 'backward'.
		"""
		if self.order != "forward":
			if self.order != "backward":
				self.order = "forward"


	def _create_cursor(self):
		"""
			Create the cursor object.
		"""
		try:
			self._cursor = self._conn.cursor()
			self._set_result_and_status("OK", "")
		except Exception as e:
			msg = "In SqliteMinor _create_cursor: " + str(e)
			self._set_result_and_status("FAIL" , msg)


