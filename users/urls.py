from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import SignUpView, UpdateProfile, ProfileDetailView
from django.contrib.auth.views import LoginView

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('users/me/profile/', UpdateProfile.as_view(), name="update_profile"),
    path('<str:username>', ProfileDetailView.as_view(), name="detail_profile"),
]
