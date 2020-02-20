from django.urls import path

from .views import HomePageView, CreatePostView, SearchResultsListView,ProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    
]