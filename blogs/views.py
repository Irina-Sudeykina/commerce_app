from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blogs.forms import BlogPostForm
from blogs.models import BlogPost


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


class BlogPostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy("blogs:blogpost_list")
    permission_required = "blogs.add_blogpost"


class BlogPostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy("blogs:blogpost_list")
    permission_required = "blogs.change_blogpost"

    def get_success_url(self):
        return reverse("blogs:blogpost_detail", args=[self.kwargs.get("pk")])


class BlogPostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blogs:blogpost_list")
    permission_required = "blogs.delete_blogpost"
