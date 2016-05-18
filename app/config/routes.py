"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'users'
routes['GET']['/signin'] = 'users#signin'
routes['GET']['/register'] = 'users#register'
routes['GET']['/users/new'] = 'users#new'
routes['POST']['/create'] = 'users#create'
routes['POST']['/add'] = 'users#add'
routes['POST']['/login'] = 'users#login'
routes['POST']['/description/<id>'] = 'users#description'
routes['POST']['/chang_pass/<id>'] = 'users#chang_pass'
routes['GET']['/dashboard'] = 'users#dashboard'
# routes['GET']['/dashboard/admin'] = 'users#admin'
routes['GET']['/users/edit'] = 'users#edit'
routes['GET']['/users/edit/<id>'] = 'users#adminedit'
routes['POST']['/users/update/<id>'] = 'users#update' 
routes['GET']['/logout'] = 'users#logout'
routes['POST']['/users/destroy/<id>'] = 'users#destroy' 

routes['GET']['/users/show/<id>'] = 'messages#index'
routes['POST']['/postmsg/<id>'] = 'messages#postmsg'

routes['POST']['/postcmt/<message_id>/<receiver_id>'] = 'comments#postcmt'

