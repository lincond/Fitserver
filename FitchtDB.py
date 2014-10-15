import MySQLdb as mdb
import sys

# ---------------- Fitcht Server Code ----------------- #
#
# 		This code is under GNU GPL license
# 		and was made to handle database operations
# 		of FitServer... please, buy me a coke if
# 		Fitcht already saved your life in something 
#					you needed.
#
#						:)
# ----------------------------------------------------- #


class FitchtDB():

	# Starts FitchtDB class initializing MySQLdb object
	def __init__(self):

		F_HOST      = '127.0.0.1'
		F_USERNAME  = 'fitcht'
		F_PASS      = 'something'
		F_DBNAME    = 'Fitcht'

		try:
			self.conn = mdb.connect(F_HOST, F_USERNAME, F_PASS, F_DBNAME)
		except:
			print 'Unable to connect to DB'


	# This Method Register a new Server
	def registerServer(self, nameServer, IPServer):

		try:
			cursor = self.conn.cursor()
			query = "INSERT INTO Servers (Name, IP) VALUES ('%s', '%s');" % (nameServer, IPServer)
			cursor.execute(query)
			self.conn.commit()
		except:
			print 'Failed to register the server. We are working on it.'


	# This Method drops the Server
	def dropServer(self, IPServer):
		
		try:
			cursor = self.conn.cursor()
			query = "UPDATE Servers SET Active = '0' WHERE IP = '%s';" % IPServer
			cursor.execute(query)
			self.conn.commit()
		except:
			print 'Could not drop the Server. We are working on it.'


	# This Method Reports the server
	def reportServer(self, IPServer):
		try:
			cursor = self.conn.cursor()
			query = "UPDATE Servers SET Report=Report+1 WHERE IP = '%s';" % IPServer
			cursor.execute(query)
			self.conn.commit()
		except:
			print 'Could not Report Server. We are working on it.'

