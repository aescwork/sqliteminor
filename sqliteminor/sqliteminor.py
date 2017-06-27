"""

..	currentmodule:: sqliteminor
	:platform: Unix, Windows
	:synopsis:  simple class template

.. moduleauthor:: Vollund Leysing  aescwork@protonmail.com


"""

import os
import sys

class SQLiteMinor(object):


	def __init__(self, db_file_path=None, conn=None):

		"""

		Args: 
			db_file_path (str):	The path to the database file with which this object will be working.

		"""
		self.result = "OK"
		self.status = ""
		self.order = "forward"	# must be either 'forward' (entries returned first to last) or 'backward' (entries returned last to first)
		self.table = None
		self.db_file_path = db_file_path
		self.conn = conn		# create the connection outside of this class ... like with an object of the sqlitemgr class (see README.txt).
		self.statement = ""
		self. = ""
		self. = ""


	def __del__(self):
		"""
			Define the __del__ (delete) magic method here.
		"""
		self.conn.close()


	@property
	def order(self):
		""" 
		Get the order (call it directly: obj.order)
		"""
		return self.order


	@order.setter
	def order(self, val):
	"""
	Set the order (directly: obj.order = "forward")
	"""

	#	try: don't need?
			self.order = val
			if self.order != "forward":
				if self.order != "backward":
					self.order = "forward"

	#	except Exception as e: don't need?
						


	def create_row(members, table=None):
	"""
	Create a row in the table whose name is assigned to self.table.
			_set_result_and_status( , )
	"""
		if table:
			self.table = table

		if self.table:
			self.statement = "INSERT INTO " + self.table + " VALUES(
		else:
			_set_result_and_status("FAIL" ,"Value for table has not been set.")
			
	
	def read_range(frm, to):


	def read_head(number):


	def read_tail(number):


	def read_rows(column_id, search_val):


	def read_search(column_id, search_val):


	def read_single_field(ref_column_id, ref_column_val, target_column_id):

	
	def read_alt_table_referant(alt_table, search_vals):
	"""
	Args:
	
		search_vals (list):	
	"""


	def update(ref_column_id, ref_column_val, target_column, updated_val):
		

	def delete(ref_column_id, ref_val):



	def _set_result_and_status(self, result, status):
		"""
		Set self.result and self.status here to help DRY out the code in the above methods.
		
		Args:
			result (string):	the result of the operation performed by the calling method.
			status (string):	the status (description) of the outcome of the operation performed by the calling method.
		"""
		self.result = result
		self.status = status


