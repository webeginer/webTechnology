from django.conf.urls import url
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
	# ex:  /ask/
	url(r'ask/', views.ask_add, name='ask_add'),
	# ex: /question/5/
	url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
]

