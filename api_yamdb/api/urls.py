from django.urls import include, path
from rest_framework import routers

from .views import (APIObtainToken, APISignUp, CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewViewSet, TitleViewSet, UsersViewSet)

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UsersViewSet, basename="users")
router.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet,
    basename="reviews",
)
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)
router.register("titles", TitleViewSet)
router.register("genres", GenreViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("v1/auth/token/", APIObtainToken.as_view(), name="obtain_token"),
    path("v1/", include(router.urls)),
    path("v1/auth/signup/", APISignUp.as_view(), name="signup"),
]
