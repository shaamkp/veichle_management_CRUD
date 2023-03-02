from django.urls import re_path, path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from api.v1.accounts import views


app_name = "api_v1_accounts"


urlpatterns = [
    re_path(r'^login-user-profile/$', views.login_user_profile),
    re_path(r'^login-admin-profile/$', views.login_admin_profile),
    re_path(r'^login-super-admin-profile/$', views.login_super_admin_profile),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]