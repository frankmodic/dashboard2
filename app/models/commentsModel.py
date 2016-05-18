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

class commentsModel(Model):
	def __init__(self):
		super(commentsModel, self).__init__()
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

	def grab_comments(self, id):
		fetch_comments = "SELECT users.id, CONCAT(users.first_name, ' ', users.last_name) AS comment_author, comment, comments.created_at, comments.message_id FROM USERS JOIN comments ON users.id = comments.user_id ORDER BY comments.created_at ASC"
		return self.db.query_db(fetch_comments)


	def postcmt(self, user_info):
		time = strftime('%B %d, %Y, %T')
		# cmt_errors = []
		# if not user_info['comment']:
		# 	cmt_errors.append('Comment field cannot be blank!')
		# if cmt_errors:
		# 	return {"status": False, "cmt_errors": cmt_errors }
		# else:
		comment_query = "INSERT INTO comments (user_id, message_id, comment, message_receiver_id, created_at) VALUES (:user_id, :message_id, :comment, :message_receiver_id, NOW())"
		data = {
			'user_id': user_info['user_id'],
			'message_id': user_info['message_id'],
			'comment': user_info['comment'],
			'message_receiver_id': user_info['message_receiver_id'],
			'created_at': time
		}
		return self.db.query_db(comment_query, data)
		return True

