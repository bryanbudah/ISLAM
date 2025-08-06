from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Course, Event, Category, QuranQuote
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Home view
def home(request):
    recent_articles = Article.objects.filter(published=True).order_by('-created_at')[:3]
    upcoming_events = Event.objects.filter(published=True).order_by('event_date')[:3]
    featured_courses = Course.objects.filter(published=True).order_by('-created_at')[:3]
    daily_quote = QuranQuote.objects.order_by('?').first()
    
    context = {
        'recent_articles': recent_articles,
        'upcoming_events': upcoming_events,
        'featured_courses': featured_courses,
        'daily_quote': daily_quote,
    }
    return render(request, 'content/home.html', context)

# Article Views
class ArticleListView(ListView):
    model = Article
    template_name = 'content/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    
    def get_queryset(self):
        return Article.objects.filter(published=True).order_by('-created_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'content/article_detail.html'
    context_object_name = 'article'

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'content/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10
    
    def get_queryset(self):
        return Course.objects.filter(published=True).order_by('-created_at')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'content/course_detail.html'
    context_object_name = 'course'

# Event Views
class EventListView(ListView):
    model = Event
    template_name = 'content/event_list.html'
    context_object_name = 'events'
    paginate_by = 10
    
    def get_queryset(self):
        return Event.objects.filter(published=True).order_by('event_date')

class EventDetailView(DetailView):
    model = Event
    template_name = 'content/event_detail.html'
    context_object_name = 'event'

# Category Views
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'content/category_detail.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        context['articles'] = Article.objects.filter(category=category, published=True)
        context['courses'] = Course.objects.filter(category=category, published=True)
        context['events'] = Event.objects.filter(category=category, published=True)
        return context

# Quran Quote View
class QuranQuoteListView(ListView):
    model = QuranQuote
    template_name = 'content/quran_quote_list.html'
    context_object_name = 'quotes'
    paginate_by = 20
    ordering = ['-created_at']

# Search View
def search(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        # Search across multiple models
        articles = Article.objects.filter(title__icontains=query, published=True)
        courses = Course.objects.filter(title__icontains=query, published=True)
        events = Event.objects.filter(title__icontains=query, published=True)
        results = list(articles) + list(courses) + list(events)
    
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'content/search.html', context)
class CustomLoginView(LoginView):
    template_name = 'registration/login.html' # Custom template location
    redirect_authenticated_user = True  # Redirects if already logged i
success_url = reverse_lazy('home')

def form_valid(self, form):
        """Security check complete, log the user in"""
        return super().form_valid(form)

class HomeView(TemplateView):
    template_name = 'content/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context here
        return context