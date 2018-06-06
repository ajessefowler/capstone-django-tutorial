from django.urls import path
from . import views

'''
	This routes the URLs for the polls application. URLs here begin with /polls/. 
	These paths lead to the views contained in views.py. <int:question_id> refers to the 
	question_id of the question that was clicked. For example, the links in index.html 
	pass the question.id to the detail view, and the detail view for that question is displayed.

'''

app_name = 'polls'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]