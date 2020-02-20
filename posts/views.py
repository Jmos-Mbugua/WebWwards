from django.shortcuts import render


from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm, ProfileForm


from .models import Post, Profile
# Create your views here.
class HomePageView(ListView):
    model = Post
    print(model)
    template_name = 'home.html'
    


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


class SearchResultsListView(ListView): # new
    model = Post
    context_object_name = 'post_list'
    template_name = 'home.html'  

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Post.objects.filter(
        Q(profile__username__icontains=query)
        ) 


class ProfileView(ListView):
    model = Profile
    template_name = 'profile.html'



