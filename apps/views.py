from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import CourseCategory, Course, Video

class HomePageView(ListView):
    model = CourseCategory
    template_name = 'index.html'
    context_object_name = 'categories'


class CourseListView(ListView):
    model = Course
    template_name = 'main/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        self.category = get_object_or_404(CourseCategory, slug=self.kwargs['slug'])
        return Course.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class VideoListView(ListView):
    model = Video
    template_name = 'main/video_list.html'
    context_object_name = 'videos'

    def get_queryset(self):
        self.course = get_object_or_404(Course, pk=self.kwargs['pk'])
        return Video.objects.filter(course=self.course)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context
