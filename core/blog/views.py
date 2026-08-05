from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView

from .models import Post

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


class PostList(ListView):
    # model=Post
    queryset=Post.objects.all()
    context_object_name = "posts"
    paginate_by=2
    ordering='id'
    # template_name = "blog/post_list.html"  # افزودن این خط
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
