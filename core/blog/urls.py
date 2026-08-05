from django.urls import path 
from . import views
from django.views.generic import TemplateView
urlpatterns=[
    path('fbv_index',views.indexView,name="fbv_index"),
    path('cbv_index',views.IndexView.as_view(),name="cbv_index")

]
