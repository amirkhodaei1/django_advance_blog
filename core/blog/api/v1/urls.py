from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.api.v1.views import CategoryModelViewSet, PostModelViewSet

app_name = "api-v1"

router = DefaultRouter()
router.include_format_suffixes=False
router.register("posts", PostModelViewSet, basename="post")
router.register("categories", CategoryModelViewSet, basename="category")
# اگر در آینده اپلیکیشن دیگری مثل accounts داشتید:
# router.register("profiles", ProfileModelViewSet, basename="profile")
urlpatterns = [
    path("", include(router.urls)),
]