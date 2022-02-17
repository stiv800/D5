#from re import template
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
#from matplotlib.style import context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


from .models import *
from .filters import NewsFilter
from .forms import PostsForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context


class NewsPost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 10


    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())


    def get_queryset(self):
        return self.get_filter().qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostsForm()
        return { **super().get_context_data(**kwargs), "filter": self.get_filter()}
    

class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())


    def get_queryset(self):
        return self.get_filter().qs


    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    template_name = 'post_create.html'
    form_class = PostsForm


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    template_name = 'post_create.html'
    form_class = PostsForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
 
 
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/news')