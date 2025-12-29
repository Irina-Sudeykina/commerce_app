from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blogs.forms import BlogPostForm
from blogs.models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publication=True)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy("blogs:blogpost_list")


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy("blogs:blogpost_list")

    def get_success_url(self):
        return reverse("blogs:blogpost_detail", args=[self.kwargs.get("pk")])


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blogs:blogpost_list")
