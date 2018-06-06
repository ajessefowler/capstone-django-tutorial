from django.contrib import admin
from .models import Question

'''
	This gives the admin site access to the Question model.
'''

admin.site.register(Question)
