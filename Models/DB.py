from flask_mysqldb import MySQL

class DB(object):
	"""Initialize mysql database """
	host = "localhost"
	user = "root"
	password = "pass"
	db = "lms"
	table = ""

	def __init__(self, app):
		app.config["MYSQL_HOST"] = self.host;
		app.config["MYSQL_USER"] = self.user;
		app.config["MYSQL_PASSWORD"] = self.password;
		app.config["MYSQL_DB"] = self.db;

		self.mysql = MySQL(app)

	def cur(self):
		return self.mysql.connection.cursor()

	def query(self, q):
		h = self.cur()
	
		if (len(self.table)>0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def commit(self):
		self.query("COMMIT;")