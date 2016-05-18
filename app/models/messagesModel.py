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

class messagesModel(Model):
	def __init__(self):
		super(messagesModel, self).__init__()
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

	def grab_messages(self, id):
		fetch_messages = "SELECT messages.id AS message_id, messages.message AS message, CONCAT(users.first_name, ' ', users.last_name) AS author_name, receiver_id, messages.created_at FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE receiver_id = :id ORDER BY created_at DESC"
		data = {
			'id': id,
		}
		return self.db.query_db(fetch_messages, data)

	def postmsg(self, user_info, id):
		time = strftime('%B %d, %Y, %T')
		post_errors = []
		if not user_info['message']:
			post_errors.append('Message field cannot be blank!')
		if post_errors:
			return {"status": False, "post_errors": post_errors }
		else:
			message_query = "INSERT INTO messages (user_id, message, receiver_id, created_at) VALUES (:user_id, :message, :receiver_id, NOW())"
			data ={
				'user_id': user_info['user_id'],
				'message': user_info['message'],
				'receiver_id': user_info['receiver_id'],
				'created_at': time
			}
			return self.db.query_db(message_query, data)
			return { "status": True }

