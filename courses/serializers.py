from rest_framework import serializers
from .models import Course
# her we add Serializer to get data in database
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course                         #  models name
        fields = '__all__'                     #  field