""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
import re
from time import strftime

class usersModel(Model):
	def __init__(self):
		super(usersModel, self).__init__()
	"""
	Below is an example of a model method that queries the database for all users in a fictitious application
	
	Every model has access to the "self.db.query_db" method which allows you to interact with the database

	def get_users(self):
		query = "SELECT * from users"
		return self.db.query_db(query)

	def get_user(self):
		query = "SELECT * from users where id = :id"
		data = {'id': 1}
		return self.db.get_one(query, data)

	def add_message(self):
		sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
		data = {'message': 'awesome bro', 'users_id': 1}
		self.db.query_db(sql, data)
		return True
	
	def grab_messages(self):
		query = "SELECT * from messages where users_id = :user_id"
		data = {'user_id':1}
		return self.db.query_db(query, data)

	"""

	def create_user(self, user_info):
		# We write our validations in model functions.
		# They will look similar to those we wrote in Flask
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
		regis_errors = []
		password = user_info['password']
		# Some basic validation
		if not user_info['first_name']:
			regis_errors.append('First name cannot be blank')
		elif len(user_info['first_name']) < 2:
			regis_errors.append('First name must be at least 2 characters long')
		if not user_info['last_name']:
			regis_errors.append('Last name cannot be blank')
		elif len(user_info['last_name']) < 2:
			regis_errors.append('Last name must be at least 2 characters long')
		if not user_info['email']:
			regis_errors.append('Email cannot be blank')
		elif not EMAIL_REGEX.match(user_info['email']):
			regis_errors.append('Invalid email format!')
		if not user_info['password']:
			regis_errors.append('Password cannot be blank')
		elif len(user_info['password']) < 8:
			regis_errors.append('Password must be at least 8 characters long')
		elif user_info['password'] != user_info['pw_confirmation']:
			regis_errors.append('Password and confirmation must match!')
		# If we hit errors, return them, else return True.
		if regis_errors:
			return {"status": False, "regis_errors": regis_errors}
		else:
			# Code to insert user goes here...
			pw_hash = self.bcrypt.generate_password_hash(password)
			query = "INSERT INTO users (first_name, last_name, email, user_level, password, created_at) VALUES (:first_name, :last_name, :email, :user_level, :password, NOW())"
			# we'll then create a dictionary of data from the POST data received
			data = {
				'first_name' : user_info['first_name'],
				'last_name' : user_info['last_name'],
				'email' : user_info['email'],
				'password' : pw_hash,
				'user_level' : 1
				}
			self.db.query_db(query, data)
			# Then retrieve the last inserted user.
			get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
			users = self.db.query_db(get_user_query)
			return { "status": True, "user": users[0] }

	def login_user(self, user_info):
		login_errors = []
		if not user_info['email']:
			login_errors.append('username field cannot be blank')
		if not user_info['password']:
			login_errors.append('password field cannot be blank')
		if login_errors:
			return {"status": False, "login_errors": login_errors}

		else:	
			password = user_info['password']
			query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			user_data = {'email': user_info['email']}
			user = self.db.query_db(query, user_data)
			if user and self.bcrypt.check_password_hash(user[0]['password'], password):
				return { "status": True, "user": user[0] }
			else:
				login_errors.append("Invalid login. Username or password doesnt match our database")
				return {"status": False, "login_errors": login_errors}

	def get_users(self):
		query = "SELECT id, CONCAT(users.first_name, ' ', users.last_name) AS name, email, created_at, user_level FROM users"
		return self.db.query_db(query)

	def get_user(self, id):
		print id
		query = "SELECT id, CONCAT(users.first_name, ' ', users.last_name) AS name, email, description, created_at, user_level FROM users where id = :id"
		data = {'id': id }
		return self.db.get_one(query, data)

	def edit_user_info(self, user_info, id):
		time = strftime('%B %d, %Y, %T')
		edit_errors = []
		# Some basic validation
		if not user_info['first_name']:
			edit_errors.append('First name cannot be blank')
		if not user_info['last_name']:
			edit_errors.append('last name cannot be blank')
		if not user_info['email']:
			edit_errors.append('Email cannot be blank')
		if edit_errors:
			return {"status": False, "edit_errors": edit_errors }
		else:
			query = "UPDATE `thewalldb`.`users` SET `first_name` = :first_name, `last_name` = :last_name, `email` = :email, `updated_at` = NOW() WHERE `id` = :id"
			data = {
				'id': id,
				'first_name': user_info['first_name'],
				"last_name" : user_info['last_name'],
				"email" : user_info['email'],
				'updated_at': time
				}
			self.db.query_db(query, data)
			return { "status": True }

	def description(self, user_info, id):
		time = strftime('%B %d, %Y, %T')
		desc_errors = []
		# Some basic validation
		if not user_info['description']:
			desc_errors.append('Description cannot be blank')
		if desc_errors:
			return {"status": False, "desc_errors": desc_errors }
		else:
			query = "UPDATE `thewalldb`.`users` SET `description` = :description, `created_at` = NOW() WHERE `id` = :id"
			data = {
				'id': id,
				'description': user_info['description'],
				'created_at': time
				}
			self.db.query_db(query, data)
			return { "status": True }

	def password(self, user_info, id):
		time = strftime('%B %d, %Y, %T')
		pass_errors = []
		# Some basic validation
		password = user_info['password']
		if not user_info['password']:
			pass_errors.append('Fields cannot be blank')
		elif len(user_info['password']) < 8:
			pass_errors.append('Password must be at least 8 characters long')
		elif user_info['password'] != user_info['pw_confirmation']:
			pass_errors.append('Password and confirmation do not match!')
		if pass_errors:
			return {"status": False, "pass_errors": pass_errors }
		else:
			pw_hash = self.bcrypt.generate_password_hash(password)
			query = "UPDATE `thewalldb`.`users` SET `password` = :password, `updated_at` = NOW() WHERE `id` = :id"
			# we'll then create a dictionary of data from the POST data received
			data = {
				'id': id,
				'password' : pw_hash,
				'updated_at' : time 
				}
			self.db.query_db(query, data)
			return { "status": True }

	def delete_user(self, id):
		admin_errors = []
		if user_level < 9:
			admin_errors.append('You cannot delete this admin!')
		if admin_errors:
			return {"status": False, "admin_errors": admin_errors }
		else:
			query = "DELETE FROM users WHERE id = :id"
			data = {'id': id }
			return self.db.query_db(query, data)
			return { "status": True }