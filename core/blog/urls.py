from django.urls import include, path

from . import views

app_name = "blog"
urlpatterns = [
    # path('fbv_index',views.indexView,name="fbv_index"),
    path("", views.IndexView.as_view(), name="cbv-index"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/api", views.PostListApiView.as_view(), name="post-list-api"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit", views.PostEditView.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    # path('go_to_maktabkhooneh/<int:pk>/',views.RedirectToMaktab.as_view(),name="go_to_maktabkhooneh")
    # path('post/',views.api_post_list_view,name="post-list"),
    path("api/v1/", include("blog.api.v1.urls", namespace="api-v1")),
    path("test_weather/", views.test_weather, name="test-weather"),
]
