"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *

class users(Controller):
	def __init__(self, action):
		super(users, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('usersModel')
		self.db = self._app.db

		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self):
		"""
		A loaded model is accessible through the models attribute 
		self.models['WelcomeModel'].get_users()
		
		self.models['WelcomeModel'].add_message()
		# messages = self.models['WelcomeModel'].grab_messages()
		# user = self.models['WelcomeModel'].get_user()
		# to pass information on to a view it's the same as it was with Flask
		
		# return self.load_view('index.html', messages=messages, user=user)
		"""
		return self.load_view('index.html')
	
	def signin(self):
		return self.load_view('signin.html')

	def register(self):
		return self.load_view('register.html')

	def create(self):
		user_info = {
			"first_name" : request.form['first_name'],
			"last_name" : request.form['last_name'],
			"email" : request.form['email'],
			"password" : request.form['password'],
			"pw_confirmation" : request.form['pw_confirmation']
		}
		
		create_status = self.models['usersModel'].create_user(user_info)
		if create_status['status'] == True:
			session['id'] = create_status['user']['id'] 
			session['first_name'] = create_status['user']['first_name']
			# we can redirect to the users profile page here
			return redirect('/dashbord')
		else:
			for message in create_status['regis_errors']:
				flash(message, 'regis_errors')
			# redirect to the method that renders the form
			return redirect('/register')

	def dashboard(self):
		users = self.models['usersModel'].get_users()
		return self.load_view('dashboard.html', all_users=users)

	def edit(self):
		return self.load_view('profile.html')

	def login(self):
		user_info = {
			"email" : request.form['email'],
			"password" : request.form['password']
			}
		user = self.models['usersModel'].login_user(user_info)
		if user['status'] == True:
			session['id'] = user['user']['id'] 
			session['first_name'] = user['user']['first_name']
			session['user_level'] = user['user']['user_level']
			return redirect('/dashboard')
		# check_password_hash() compares encrypted password in DB to one provided by user logging in
		
		# Whether we did not find the email, or if the password did not match, either way return False
		else:
			if user['status'] == False:
				for message in user['login_errors']:
					flash(message, 'login_errors')
				# redirect to the method that renders the form
				return redirect('/signin')
	def new(self):
		return self.load_view('add.html')

	def add(self):
		user_info = {
			"first_name" : request.form['first_name'],
			"last_name" : request.form['last_name'],
			"email" : request.form['email'],
			"password" : request.form['password'],
			"pw_confirmation" : request.form['pw_confirmation']
		}
		
		create_status = self.models['usersModel'].create_user(user_info)
		if create_status['status'] == True:
			# we can redirect to the users profile page here
			return redirect('/dashboard')
		else:
			for message in create_status['regis_errors']:
				flash(message, 'regis_errors')
			# redirect to the method that renders the form
			return redirect('/users/new')

	def update(self, id):
		user_info = {
			"email" : request.form['email'],
			"first_name" : request.form['first_name'],
			"last_name" : request.form['last_name']
		}
		info_status = self.models['usersModel'].edit_user_info(user_info, id)
		if info_status['status'] == True:
			return redirect('/dashboard')
		else:
			if info_status['status'] == False:
				for message in info_status['edit_errors']:
					flash(message, 'edit_errors')
				# redirect to the method that renders the form
			one_user = self.models['usersModel'].get_user(id)
			return self.load_view('profile.html', one_user=one_user)
	
	def description(self, id):
		user_info = {
			"description" : request.form['description']
		}
		description_status = self.models['usersModel'].description(user_info, id)
		if description_status['status'] == True:
			return redirect('/dashboard')
		else:
			if description_status['status'] == False:
				for message in description_status['desc_errors']:
					flash(message, 'desc_errors')
				return redirect('/users/edit')

	def chang_pass(self, id):
		user_info = {
			"password" : request.form['password'],
			"pw_confirmation" : request.form['pw_confirmation']
		}
		pass_status = self.models['usersModel'].password(user_info, id)
		if pass_status['status'] == True:
			# we can redirect to the users profile page here
			return redirect('/dashboard')
		else:
			for message in pass_status['pass_errors']:
				flash(message, 'pass_errors')
			# redirect to the method that renders the form
			return redirect('/users/edit')

	def adminedit(self, id):
		one_user = self.models['usersModel'].get_user(id)
		return self.load_view('adminedit.html', one_user=one_user)

	def destroy(self, id):
		admin_status = self.models['usersModel'].delete_user(id)
		if admin_status['status'] == True:
			return redirect('/dashboard')
		else:
			if admin_status['status'] == False:
				for message in admin_status['admin_errors']:
					flash(message, 'admin_errors')
				return redirect('/dashboard')

	def logout(self):
		session.clear()
		return redirect('/')
