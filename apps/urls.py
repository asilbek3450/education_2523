from django.urls import path
from .views import HomePageView, CourseListView, VideoListView

urlpatterns = [
    path('', HomePageView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', VideoListView.as_view(), name='video_list'),
]
