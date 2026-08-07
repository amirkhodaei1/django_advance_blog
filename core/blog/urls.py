from django.urls import path 
from . import views
app_name='blog'
urlpatterns=[
    # path('fbv_index',views.indexView,name="fbv_index"),
    path('cbv_index/',views.IndexView.as_view(),name='cbv-index'),
    path('post/',views.PostListView.as_view(),name="post-list"),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
    path('post/create/',views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/edit',views.PostEditView.as_view(),name="post-edit"),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name="post-delete"),
    

    path('go_to_maktabkhooneh/<int:pk>/',views.RedirectToMaktab.as_view(),name="go_to_maktabkhooneh")
]