from django.urls import path
from .import api
app_name='courses'
urlpatterns=[
	path('api/list',api.all_course,name='course_detail'),
	#path('api/list/<id:id>',api.course_detail,name='course_detail'),

]