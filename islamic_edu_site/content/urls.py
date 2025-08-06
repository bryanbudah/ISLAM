# urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
    # Authentication
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # Courses
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),

    # Articles
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),

    # Events
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<slug:slug>/', views.EventDetailView.as_view(), name='event-detail'),
]
