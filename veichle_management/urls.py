from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Veichle Management Admin"
admin.site.site_title = "Veichle Management Admin"
admin.site.index_title = "Welcome to Veichle Management Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/accounts/', include("api.v1.accounts.urls", namespace="api_v1_accounts")),
    path('api/v1/web/', include("api.v1.web.urls", namespace="api_v1_web")),
]
