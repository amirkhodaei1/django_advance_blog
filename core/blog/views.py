from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView,UpdateView,DeleteView
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# 1. Function-Based View (برای مسیر fbv_index)
"""
def indexView(request):
    context = {"name": "Amirhossein"}
    return render(request, "blog/index.html", context)
"""


# 2. Class-Based View (برای نمایش صفحه اصلی)
class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Hossein"
        context["posts"] = Post.objects.all()
        return context


# 3. function-Based View (برای ریدایرکت)

""" 
def redirect_to_maktab_view(request, pk):
    # بررسی وجود پست (در صورت عدم وجود، خطای 404 می‌دهد)
    post = get_object_or_404(Post, pk=pk)
    print(post)
    
    # ریدایرکت موقت (HTTP 302)
    return redirect('https://maktabkhooneh.org')

    # اگر ریدایرکت دائمی (HTTP 301) مد نظر شما باشد:
    # return redirect('https://maktabkhooneh.org', permanent=True)
"""


# 3. Class-Based View (برای ریدایرکت)
class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "blog.view_post"

    # model=Post
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"
    # template_name = "blog/post_list.html"  # افزودن این خط
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "blog/post_detail.html"


# class PostFormView(FormView):
#     template_name = "contact.html"
#     form_class = PostForm
#     success_url = "/blog/post"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    form_class = PostForm
    success_url = "/blog/post"
    # fields = ["author", "title", "content", "status", "category", "published_date"]
    template_name='contact.html'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin,UpdateView):

    model=Post

    form_class = PostForm

    success_url = "/blog/post"

    # fields = ["author", "title", "content", "status", "category", "published_date"]

    template_name='contact.html'

    def form_valid(self, form):

        form.instance.author=self.request.user

        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin,DeleteView):

    model=Post
    success_url = "/blog/post"

    # fields = ["author", "title", "content", "status", "category", "published_date"]

    # template_name='contact.html'

