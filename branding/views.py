from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Branding
from .branding_generator import (
                generate_branding_snippet, 
                generate_keywords)


def home(request):
    context = { 
        'brandings': Branding.objects.all(),# key string need to the same spelling as the one in 'home.html'
    }
    return render(request, 'branding/home.html', context)

class BrandingListView(ListView):
    model = Branding 
    template_name = 'branding/home.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'brandings'
    ordering = ['-created_at']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BrandingListView, self).get_context_data(**kwargs)
        return context

class UserBrandingListView(ListView):
    model = Branding 
    template_name = 'branding/user_brandings.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'brandings'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Branding.objects.filter(author=user).order_by('-created_at')



class BrandingDetailView(DetailView):
    model = Branding 
    
class BrandingCreateView(LoginRequiredMixin, CreateView):
    model = Branding
    fields = ['topic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.branding_content=generate_branding_snippet(form.instance.topic)
        return super().form_valid(form)

class BrandingUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Branding
    fields = ['branding_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        branding = self.get_object()
        if self.request.user == branding.author:
            return True
        return False

class BrandingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Branding 
    success_url = '/'

    def test_func(self):
        branding = self.get_object()
        if self.request.user == branding.author:
            return True
        return False

def about(request):
    return render(request, 'branding/about.html', {'title': 'About'})



