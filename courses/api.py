from.models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def all_course(request):
	all_course=Course.objects.all()
	data=CourseSerializer(all_course,many=True).data
	return Response({'data':data})

@api_view(['GET'])
def course_detail(request,id):
	course_detail=Course.objects.get(id=id)
	data=CourseSerializer(course_detail).data
	return Response({'data':data})
