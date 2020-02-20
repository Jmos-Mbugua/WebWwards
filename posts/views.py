from django.shortcuts import render


from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm, ProfileForm


from .models import Post, Profile
# Create your views here.
class HomePageView(ListView):
    model = Post
    print(model)
    template_name = 'home.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, PostForm):
        PostForm.instance.user = self.request.user
        return super(CreatePostView, self).form_valid(PostForm)


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



