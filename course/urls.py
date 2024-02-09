# from .views import CourseCRUD
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('course', CourseCRUD, basename='course')
# urlpatterns = router.urls




from django.urls import path
# from .views import CourseCRUD,CourseDetailUpdateDelate
from  .views import CourseDetailUpdateDelateAPIView
app_name = 'course'
urlpatterns=[
    # path('course/',CourseCRUD.as_view(), name='courses'),
    path('course/<int:pk>', CourseDetailUpdateDelateAPIView.as_view(), name='detail-update-delate'),

]