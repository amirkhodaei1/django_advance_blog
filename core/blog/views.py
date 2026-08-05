from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView,RedirectView
from .models import Post

# Create your views here.
# FBV for show a template
'''
def indexView(request):
    """
    """
    context = {"name": "Amirhossein"}
    return render(request, "blog/index.html", context)
'''


class IndexView(TemplateView):
    """ """

    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Hossein"
        context["posts"] = Post.objects.all()
        return context


# FBV for redirect
"""
from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhoone.com')
"""
class RedirectToMaktab(RedirectView):
    url='https://maktabkhooneh.org'
    def get_redirect_url(self,*args, **kwargs):
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args,**kwargs)