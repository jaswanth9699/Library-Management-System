class UserDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "users"


	def list(self):
		users = self.db.query("select * from @table").fetchall()

		return users

	def getById(self, id):
		q = self.db.query("select * from @table where id={}".format(id))

		user = q.fetchone()

		return user

	def getByEmail(self, email):
		q = self.db.query("select * from @table where email='{}'".format(email))

		user = q.fetchone()

		return user

	def add(self, user):
		name = user['name']
		email = user['email']
		password = user['password']

		q = self.db.query("INSERT INTO @table (name, email, password) VALUES('{}', '{}', '{}');".format(name, email, password))
		self.db.commit()
		
		return q
