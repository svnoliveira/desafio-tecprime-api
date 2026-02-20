from django.urls import path
from .views import (
    CookieTokenObtainPairView,
    LogoutView,
    MeView,
    UserCreateView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("register/", UserCreateView.as_view()),
    path("me/", MeView.as_view()),
    path("users/", UserListCreateView.as_view()),
    path("users/<int:user_id>/", UserRetrieveUpdateDestroyView.as_view()),
    path("login/", CookieTokenObtainPairView.as_view()),
    path("logout/", LogoutView.as_view()),
]
