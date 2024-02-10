from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CourseSerializer
from .models import Course
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, status


# Create your views here.

# class CourseCRUD(generics.ListCreateAPIView):
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all().order_by("-create_at")
#     lookup_field = "pk"
#
# class CourseDetailUpdateDelate(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()
#     lookup_field = "pk"



# class CourseCRUD(viewsets.ModelViewSet):
#     serializer_class = CourseSerializer
#     queryset =Course.objects.all().order_by("-create_at")
#     lookup_field = "pk"



class CourseDetailUpdateDelateAPIView(APIView):
    def get(self,request,pk):
        course=Course.objects.get(pk=pk)
        serializer=CourseSerializer(course)
        return Response(data=serializer.data)

    def delete(self,request,pk):
        course=Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        course = Course.objects.get(pk=pk)
        serializer=CourseSerializer(instance=course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        course = Course.objects.get(pk=pk)
        serializer=CourseSerializer(instance=course,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
