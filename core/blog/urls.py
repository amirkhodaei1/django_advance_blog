from django.urls import path 
from . import views
from django.views.generic.base import RedirectView
app_name='blog'
urlpatterns=[
    # path('fbv_index',views.indexView,name="fbv_index"),
    path('cbv_index',views.IndexView.as_view(),name='cbv-index'),
    path('post/',views.PostList.as_view(),name="post-list"),

    path('go_to_maktabkhooneh/<int:pk>/',views.RedirectToMaktab.as_view(),name="go_to_maktabkhooneh")
]