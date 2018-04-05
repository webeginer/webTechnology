from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# urlpatterns = [
# 	url(r'^$', views.test),
# ]

app_name = 'qa'
urlpatterns = [
	# ex: /
	url(r'^$', views.index, name='index'),
	# ex: /popular/
	url(r'popular/', views.popular, name='popular'),
	# ex: /question/5/
	url(r'question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
	# ex:  /ask/
	url(r'ask/', views.ask_add, name='ask_add'),
	# ex:  /signup/
	url('signup/', views.signup, name='signup'),
	# ex:  /login/
	url('login/', auth_views.login, name='login'),
	# ex:  /logout/
	url('logout/', auth_views.logout, {'next_page': 'qa:index'}, name='logout'),
]