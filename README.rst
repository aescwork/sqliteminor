SQLiteMinor
========================

SQLiteMinor is a simple Python class for reading- and deleting from, updating and adding to a table in an sqlite database. 

The SQLiteMinor object provides basic database table access functionality without the need for writing any sql statements,
writing code for connection and cursor objects, etc.  The operations are handled with simple method calls on the
object.  The functionality is also limited, as the sql statements which are used to work with the database are mostly fixed;
therefore the name of this module is "minor".  

The main goal of writing this module was to provide a means of working with sqlite databases without the user/developer having 
to actually write any sql or python code which directly executes it. Instead, the object and methods make what is hopefully a
cleaner and more intuitive interface.  Naturally there is also the advantage of having most or all the sql/python database code needed
in one class.

This module was written as a companion to the sqlitemgr module (https://github.com/aescwork/sqlitemgr).  

This module was originally conceived for the waxtablet Python application, along with the FileWork module (https://github.com/aescwork/filework)
and the sqlitemgr module (https://github.com/aescwork/sqlitemgr).  

Complete documentation for this module is available in the docs/ directory of this repository.  The main page of the documentation is in docs/index.html.
Also look for the usage.html page for a basic explanation of how to use the class.


After installation of this package is complete, trying to use the module might result in the following error: "ImportError: No module named sqlitemgr"
or some other error message.

This probably indicates that the Python interpreter may not be able to locate the module.  In this case,
the following is recommended:

	On Linux:

		Locate where the package was installed.  In the terminal, navigate to the root directory and execute the following command:

												sudo find . -name sqliteminor.py


		This should give a path to the sqliteminor.py file.  
		Create a file called "local_python.sh" and put the following text in it:

								PYTHONPATH="/usr/local/lib/python*.*/dist-packages/sqliteminor/":"${PYTHONPATH}"
								export PYTHONPATH

		To make the module available to all users, place this file in /etc/profile.d.  Then place a line to execute this
		file somewhere in .bashrc or one of the other bash configuration files in the individual (non-root) user's terminal: 

										    . /etc/profile.d/local_python.sh

		This should cause the python interpreter to locate the sqliteminor.py file in the module.   


