"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class comments(Controller):
	def __init__(self, action):
		super(comments, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('messagesModel')
		self.load_model('usersModel')
		self.load_model('commentsModel')
		self.db = self._app.db

		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self, id):
		one_user = self.models['usersModel'].get_user(id)
		all_messages = self.models['messagesModel'].grab_messages(id)
		all_comments = self.models['commentsModel'].grab_comments(id)
		print ALL_comments
		return self.load_view('wall.html', one_user=one_user, all_messages=all_messages, all_comments=all_comments)

	def postcmt(self, message_id, receiver_id):
		user_info = {
			"user_id" : session['id'],
			"comment" : request.form['comment'],
			"message_receiver_id" : message_id,
			'message_id': message_id
		}
		self.models['commentsModel'].postcmt(user_info)
		print comments
		return redirect('/users/show/'+receiver_id)
		# if postcmt_status['status'] == True:
		# 	return redirect('wall.html')
		# else:
		# 	if postcmt_status['status'] == False:
		# 		for message in postcmt_status['cmt_errors']:
		# 			flash(message, 'cmt_errors')
		# 		return redirect('messages/index')
		