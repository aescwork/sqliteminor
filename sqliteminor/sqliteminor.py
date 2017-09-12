"""

..	currentmodule:: sqliteminor
	:platform: Unix, Windows
	:synopsis:  a python wrapper class for reading, updating, and deleting from tables of an sqlite database

.. moduleauthor:: aescwork aescwork@protonmail.com


"""



class SQLiteMinor(object):


	def __init__(self, conn=None, table=None):

		"""

		Args: 
			db_file_path (str):			The path to the database file with which this object will be working.
			conn (Sqlite3.Connection):	A connection object for interfacing with an sqlite database.

		"""
		self.result = "None"
		self.status = "None"
		self.table = table
		self._conn = conn # create the connection outside of this class ... maybe with an object of the sqlitemgr class (see README.txt).
		self._cursor = None

		if conn:
			self._create_cursor()

	def __del__(self):
		
		if str(type(self._conn)) == "<type 'sqlite3.Connection'>":        
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


	@property
	def cursor(self):
		""" 
		Get the conn (call it directly: obj.cursor)
		"""
		return self._cursor

	
	def add(self, members):
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

		Returns:
				Number of rows added or None if there was a problem executing the statement.

		.. warning::
									This method as written can only execute one INSERT at a time.

		.. note::
									If adding a row which contains a date, be sure to render the date in the YYYY-MM-DD format.
									Example: '2017-05-20'.  The date can be either a string (corresponding to the TEXT data type in an 
									sqlite table) or a datetime.date object (corresponding to the DATE data type in an sqlite table).
		"""

		placeholders = "("
		c = 1
		for m in members:						
			if c == len(members): 
				placeholders = placeholders + "?)"
			else:
				placeholders = placeholders + "?, "
			c = c + 1

		return self.exec_stat("INSERT INTO " + self.table + " VALUES" + placeholders, "add", (members))



	def read_all(self, select_column="*"):
		"""
		Retrieve all rows from the table.

		Args:
				select_column (str), (list):	The column(s) of the row from which to retrieve.  The column name(s) passed in with select_column 
												will be the only column data returned from the row.  select_column can be either a single value (str), or a list
												(of strings) for retrieving from multiple columns. The default is "*", which returns every column in a row.								
		Returns:
			rows (list): A list containing each row retrieved or None if there was a problem executing the statement.
	
		"""

		if type(select_column) is list:
			select_column = ', '.join(select_column)
	
		return self.exec_stat("SELECT " + select_column + " FROM " + self.table,  "read_all")



	def read_range(self, frm, to, col,  select_column="*"):
		"""
		Retrieve a group of rows from a table whose data in a specified column (col) falls within a certain range.  The range is assessed
		as being composed of values between a greater-than- and a less-than- reference value: 'frm' and 'to'.  
		
		.. note:
				If the 'frm' and 'to' arguments are strings, a modulo or percent sign (%) can be pre- and/or appended 		
				to these arguments when they are passed in (like "%lucky%" or "%wild", etc).   
				If the modulo is on both sides of the argument ("%lucky%"), then if the argument matches anywhere in the searched column, 
				the row will be retrieved.
				If the modulo is prepended to the argument ("%lucky"), then if the argument appears at the beginning of the searched column, 
				the row will be retrieved.
				If the modulo is appended to the argument ("lucky%"), then if the argument appears at the end of the searched column, 
				the row will be retrieved.

				Generally, using (or not using) the modulo can affect whether the rows containing the reference values are included in the search result.
				Using them may give a more inclusive result.

		Args:
				frm (str) (int), (datetime.date) ...(others):	"from", the starting value of the range of values to be retrieved.  
				to (str) (int), (datetime.date) ...(others):	the ending value of the range of values to be retrieved.  
				col (str) (int), (datetime.date) ...(others):	the actual name of the column of the table where the values are stored.
				select_column (str), (list):	The column(s) of the row from which to retrieve.  The column name(s) passed in with select_column 
												will be the only column data returned from the row.  select_column can be either a single value (str), or a list
												(of strings) for retrieving from multiple columns. The default is "*", which returns every column in a row.								

		Returns:
				rows (list): A list containing each row retrieved  or None if there was a problem executing the statement.

		.. note:
				Values are returned according to the type they are stored as in the table.  For instance, if a date is stored in a column
				whose sqlite type is DATE, a (python) datetime.date object will probably be returned.  Handle accordingly.  Moreover, values of different
				data types may be passed in with 'frm' and 'to' -- as long as they correspond with the data type of the column of the sqlite
				table, the SELECT statement should work.
		"""

		
		if type(select_column) is list:
			select_column = ', '.join(select_column)
	

		statement = "SELECT " + select_column + " FROM " + self.table + " WHERE " + col + " BETWEEN ? AND ?"

		return self.exec_stat(statement, "read_range", (frm, to)) 


	def read_head(self, number=5,  select_column="*"):
		"""
		Retrieve the first n rows in the table.

			Args:
				number (int):	the number of rows from the top of the table to be returned.
				select_column (str), (list):	The column(s) of the row from which to retrieve.  The column name(s) passed in with select_column 
												will be the only column data returned from the row.  select_column can be either a single value (str), or a list
												(of strings) for retrieving from multiple columns. The default is "*", which returns every column in a row.								

			Returns:
				rows (list): A list containing each row retrieved  
								or None if there was a problem executing the statement.

		"""
		if type(select_column) is list:
			select_column = ', '.join(select_column)

		return self.exec_stat("SELECT " + select_column + " FROM " + self.table + " LIMIT ?", "read_head", (number, ))



	def read_tail(self, number=5, col=None, select_column="*"):
		"""
		Retrieve the last n rows in the table.

			Args:
				number (int):	the number of rows from the top of the table to be returned.
				col    (str):	the name of a column in the table which the sql statement needs as a reference. This should be a
								column that contains an ID number for the row, in order to actually get the last n rows from the table.

								If this is not passed in, the _ROWID_ column is used.
				select_column (str), (list):	The column(s) of the row from which to retrieve.  The column name(s) passed in with select_column 
												will be the only column data returned from the row.  select_column can be either a single value (str), or a list
												(of strings) for retrieving from multiple columns. The default is "*", which returns every column in a row.								

			Returns:
				rows (list): A list containing each row retrieved or None if there was a problem executing the statement.


		"""
		if not col:
			col = "_ROWID_"

		if type(select_column) is list:
			select_column = ', '.join(select_column)
			
		return self.exec_stat("SELECT " + select_column + " FROM " + self.table + " ORDER BY " + col + " DESC LIMIT ?", "read_tail", (number, ))


	def read_search_rows(self, target_col, search_val, search_scope="has-any", select_column="*"):

		"""
		Retrieve one or more rows whose specified column has the passed-in value.  

		Args:
				target_col (str)(list):					 The name of the column to be searched for the value in search_val.  If its a list,
															then target_col must contain two or more column names to be inspected.

				search_val (str) ...(other)(list): 		 The value to search for in the column specified by col.  If its a list, then
															search_val must contain two or more search values to look for in the column or columns.

				search_scope (str):		Determines how the sql statement tells sqlite to evaluate the search conditions when searching for multiple
										search values and/or in multiple columns.  This is done by using the value of search_scope to specify 
										the logical operator in the sql to use for the search: AND or OR.
										Possible values:
											"has-any" - If a row fulfills any of the conditions specified in the ref_col and/or ref_col_val lists, it 
														qualifies.  Permissive: any row who has any of the search values in the specified column(s) will be 
														subjected to the action.
											"has-all" - If (and only if) a row fulfills all of the conditions specified in the ref_col and/or 
														ref_col_val lists, it qualifies. Strict: only a row which has all of the search values in
														the specified column(s) will be subjected to the action.

				select_column (str), (list):	The column(s) of the row from which to retrieve.  The column name(s) passed in with select_column 
												will be the only column data returned from the row.  select_column can be either a single value (str), or a list
												(of strings) for retrieving from multiple columns. The default is "*", which returns every column in a row.								

		.. note:
				If the 'target_col' and 'search_val' arguments are strings (or lists of strings), a modulo or percent sign (%) can be pre- 
				and/or appended	to these arguments (or list elements) when they are passed in (like "%lucky%" or "%wild", etc).   
				If the modulo is on both sides of the search term ("%lucky%"), then if the search term matches anywhere in the searched column, 
				the row will be retrieved.
				If the modulo is prepended to the search term ("%lucky"), then if the search term appears at the beginning of the searched column, 
				the row will be retrieved.
				If the modulo is appended to the search term ("lucky%"), then if the search term appears at the end of the searched column, 
				the row will be retrieved.

				Generally, using (or not using) the modulo can affect whether the rows containing the reference values are included in the search result.
				Using them may give a more inclusive result.
		Returns:

			rows (list): A list containing each row retrieved or None if there was a problem executing the statement.

	
		"""
		if type(select_column) is list:
			select_column = ', '.join(select_column)

		stmt_parts = self._make_operator(target_col, search_val, search_scope)

		return self.exec_stat("SELECT " + select_column + " FROM " + self.table + stmt_parts[0], "read_search_rows", stmt_parts[1])

	
	def read_by_date_part(self, part, column, search_val, select_column="*"):
		"""
		A method for specifically working with dates. Retrieve one or more rows whose date has the passed-in day, month or year.  

		Args:
				part (str):			Possible values are "day", "month" or "year".  This specifies which part of the date to search by.
				column (str):   	The name of the column containing the date.
				search_val (str):   The numerial value for the day (calendar date), month or year.  

		.. warning:
				This method assumes that the column which holds the date is of the DATE data type.  When the date is stored in a column of the 
				DATE data type, it must be a string of the format YYYY-MM-DD, or year-month-day.  Example: '2017-04-12'.  
				When the date is retrieved from the table, it will be returned as a python datetime.date object.  
				Handle accordingly. (In other words, remember to include the datetime module in your code, or convert the datetime value returned to
				a string, etc.).  
				
		
		"""
		if type(select_column) is list:
			select_column = ', '.join(select_column)

		subs = {"year":"%Y", "month":"%m","day":"%d"}
		
		return self.exec_stat("SELECT " + select_column + " FROM " + self.table + " WHERE strftime('" + subs[part] +"', datetime(" + column + ")) = ?", \
				"read_by_date_part",  (search_val, ))


	def update(self, target_col, new_val, ref_col, ref_col_val):

		"""
		Update a value in a column of one or more rows in the table.
		
		Args:
			target_col (str), (list):		The name of the column(s) which is to receive the new (updated) value(s).  This can also be a list of column-names.
			new_val (...), (list):			The new value for the target_col.  This can also be a list of values.  If this and target_col are lists, 
											the new_val list should match up one-to-one with with the target_col list.  
			ref_col (str):					The column whose value is to be used as a reference for finding the column of the row(s) to modify.
			ref_col_val (str):				The value the ref_col is to have to indicate its row is to be modified.


		Returns:
				Number of rows modified or None if there was a problem executing the statement.

		"""
		
		if type(target_col) is not list:
			target_col = [target_col]
		if type(new_val) is not list:
			new_val = [new_val]

		statement = ""
		i = 0
		j = len(target_col)
		for col in target_col:
			statement = statement + str(col) + " = " +  "?"
			if j > 1:
				statement = statement + ", "
			i = i + 1
			j = j - 1
		
		new_val.append(ref_col_val)

		return self.exec_stat("UPDATE " + self.table + " SET " + statement + " WHERE " + ref_col + " LIKE ?",  "update", tuple(new_val))


	def delete(self, ref_col, ref_col_val, search_scope="has-any"):

		"""
		Delete one or more rows in the table.

		Args:
			ref_col	(str), (list):		The column whose value is to be used as a reference for finding the column of the row(s) to modify.  Can be a
								
			ref_col_val (str), (list):	The value the ref_col is to have to indicate its row is to be deleted.

			search_scope (str):	Determines how the sql statement tells sqlite to evaluate the search conditions when searching for multiple
								search values and/or in multiple columns.  This is done by using the value of search_scope to specify 
								the logical operator in the sql to use for the search: AND or OR.
								Possible values:
								"has-any" - If a row fulfills any of the conditions specified in the ref_col and/or ref_col_val lists, it 
											qualifies.  Permissive: any row who has any of the search values in the specified column(s) will be 
											subjected to the action.
								"has-all" - If (and only if) a row fulfills all of the conditions specified in the ref_col and/or 
											ref_col_val lists, it qualifies. Strict: only a row which has all of the search values in
											the specified column(s) will be subjected to the action.
			.. note:
					The search_scope variable is only evaluated if ref_col and/or ref_col_val are lists.

		Returns:
				Number of rows modified or None if there was a problem executing the statement.

		.. note:
				if search_to_right/search_to_left are used and exact_match is False, this method is best suited for searching strings.
		"""

		stmt_parts = self._make_operator(ref_col, ref_col_val, search_scope)
		
		return self.exec_stat("DELETE FROM " + self.table + stmt_parts[0], "delete", stmt_parts[1])

	
	def exec_stat(self, statement, method_name, param_tuple=None):

		"""

		General code for executing the queries for all of the methods.  Also allows a custom sql statement provided by the 
		calling code to be executed.

		Args:
				statement (str):	The statement to be executed.
				method_name(str):	The name of the calling method.

		Returns:
				rows (if a SELECT statement)
				number of rows affected/added (if a DELETE or UPDATE)
				None (if there was a problem with the execution of the statement)		
		"""

		ret_val = None
	
		try:
			if param_tuple:
				self._cursor.execute(statement, param_tuple)
			else:
				self._cursor.execute(statement)

			if "SELECT" in statement:
				ret_val = self._cursor.fetchall()
				ret_val.sort()
			else:
				self.conn.commit()
				ret_val = self._cursor.rowcount

			self._set_result_and_status("OK", "")

		except Exception as e:
			msg = "In sqliteminor " + method_name + "(): " + str(e)
			self._set_result_and_status("FAIL", msg)

	
		return ret_val


	def _make_operator(self, col, val, search_scope):
		"""
			Create and return the variable part of the sql statement where there are multiple columns to
			inspect and/or multiple search values to look for.
			Used by read_search_rows() and delete() for SELECTing or DELETEing one or more rows in a table.

			Args:
				col (str) (list):		A list containing the columns to search.
				val (str) (list):		A list containing one or more search terms to look for in each column.  If there is
										only one term to search for in a column, then each term will match one to one with
										the columns listed in col.	If there are multiple terms to search for in each column,
										then val can contain nested lists.  Each column-name in col would match each nested list
										in val.
										Example: col could have two columns ["name", "description"]
										and val would have two terms: ["Ash", "European"].  

																or
							
										Example: col could have two columns ["name", "description"]
										and val could have a nested list for possible values to search for in the 'name' column, and
										a nested list for possible values to search for in the 'description' column:
										[["Ash", "Yew", "White Pine"], ["needles", "European", "leaves"]].

			Returns:
					list [statement_part, parameter_tuple]

		"""

		statement = " WHERE "
		ret_tuple = list()

		# if either col or val is not a list, put them in lists
		if type(col) is not list:
			col = [col]

		if type(val) is not list:
			val = [val]

		if search_scope == "has-any":
			operator = "OR"
		elif search_scope == "has-all":
			operator = "AND"

		i = 0
		# THIS IS WRONG -- COPY OVER FROM waxtablet
		for v in val:
			if type(v) is list:
				for nv in v:
					statement = statement + col[i] + " LIKE ? " + operator + " "
					ret_tuple.append(nv)
			else:
				statement = statement + col[i] + " LIKE ? " + operator + " "
				ret_tuple.append(v)
			i = i + 1
		
		if operator == "AND":
			s = statement[:-5]		# get rid of the last operator from the statement
		elif operator == "OR":
			s = statement[:-4]		# get rid of the last operator from the statement

		return [s, tuple(ret_tuple)]



	def _set_result_and_status(self, result, status):
		"""
		Set self.result and self.status here to help DRY out the code in the above methods.
		
		Args:
			result (self, string):	the result of the operation performed by the calling method.
			status (self, string):	the status (self, description) of the outcome of the operation performed by the calling method.
		"""
		self.result = result
		self.status = status


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





