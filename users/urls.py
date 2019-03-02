from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import LoginFormView, SignUpView, UpdateProfile

app_name = "users"

urlpatterns = [
    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('users/me/profile/', UpdateProfile.as_view(), name="update_profile"),
]
