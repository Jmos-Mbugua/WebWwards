from django.urls import path

from .views import ApiPostListView, ApiPostDetailView, ApiProfileListView, ApiProfileDetailView

urlpatterns = [
    path('', ApiPostListView.as_view(), name='post_list'),
    path('<int:pk>/', ApiPostDetailView.as_view(), name='single_post'),
    path('<int:pk>/', ApiProfileListView.as_view(), name='profile_list'),
    
]