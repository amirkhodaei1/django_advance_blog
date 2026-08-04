from django.urls import path 
from .views import *
from django.views.generic import TemplateView
urlpatterns=[
    path('fbv_index',indexView,name="fbv_index"),
    path('cbv_index',TemplateView.as_view(template_name='blog/index.html',extra_context={"name":"Hoseein"}))

]