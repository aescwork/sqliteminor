SQLiteMinor
========================

This package can be found at https://github.com/aescwork/sqliteminor. 
 
In the github repository there is sphinx-generated documentation: the main page is docs/index.html. Included in the documentation is a Usage
file (docs/usage.html) which provides a simple and hopefully helpful explanation about how the methods work and how to call them.



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


	On MS Windows:
		
		The following was tested on a machine running Windows 10. 
		
		(This assumes that Python is installed on the machine.)

		Locate where the package was installed.  On Windows 10, Look for the Python folder.  Its usually right under the C: drive. 
		The name of the folder probably has the version number in it as well, like "Python27".  Look for the sqliteminor folder: it should
		be in "Lib\" and then "site-packages\" folder.  

		Open up the System Properties Panel.  (You can find this by clicking on the "Settings" icon and entering "Environment Variables" in the 
		search bar.  When the panel comes up, Click the "Environment Variables" button.  Under "System variables", click "New" and type in the full path to
		the sqliteminor folder.

		Test this by opening the command line application and starting the Python interpreter (type the command "python" and press enter).
		Now try to import the module and instantiate an sqliteminor object.  Type the following:
	
		>>> import sqliteminor
		>>> sg = sqliteminor.SQLiteMinor()
		>>> sg.result

		If everything went well, 'None' should print out on the screen.  If there was an "ImportError" or any other error, try importing the
		module again and test as follows: 


		>>> import sqliteminor.sqliteminor as sqliteminor
		>>> sg = sqliteminor.SQLiteMinor()
		>>> sg.result


