import pandas as pd
import pyodbc
import sys


def sql_server_pull():
    # Trusted connection allows for Windows authentication
	try:
		connection = pyodbc.connect(r'Driver={SQL Server Native Client 11.0};'
									r'Server=*****;'
									r'Database=*****;'
									r'trusted_connection=yes'
									)
	except pyodbc.Error:
		print("Connection Error")
		sys.exit()

	cursor = connection.cursor()
	SQLCommand = ("""
		SELECT *
		  FROM Database;
	""")

	cursor.execute(SQLCommand)
	results = cursor.fetchall()

	df = pd.DataFrame.from_records(results)
	connection.close()

	try:
		df.columns = pd.DataFrame(np.matrix(cursor.description))[0]
		df.drop_duplicates(inplace=True)
	except:
		df = None
		print('Dataframe is empty')

	return df
