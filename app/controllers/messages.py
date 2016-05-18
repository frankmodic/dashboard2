"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class messages(Controller):
	def __init__(self, action):
		super(messages, self).__init__(action)
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
		print all_messages
		return self.load_view('wall.html', one_user=one_user, all_messages=all_messages, all_comments=all_comments)

	def postmsg(self, id):
		user_info = {
			"user_id" : session['id'],
			"message" : request.form['message'],
			"receiver_id" : id
		}
		postmsg_status = self.models['messagesModel'].postmsg(user_info, id)
		if postmsg_status['status'] == True:
			one_user = self.models['usersModel'].get_user(id)
			return self.load_view('wall.html', one_user=one_user)
		else:
			if postmsg_status['status'] == False:
				for message in postmsg_status['post_errors']:
					flash(message, 'post_errors')
				return redirect('/index')
		
		