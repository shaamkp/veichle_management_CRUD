from django.urls import re_path

from api.v1.web import views

app_name = "api_v1_web"

urlpatterns = [
    re_path(r'^create/veichle-details/$',views.add_veichle_details),
    re_path(r'^read/veichle-details/$',views.veichle_details),
    re_path(r'^update/veichle-details/(?P<pk>.*)/$',views.edit_veichle_details),
    re_path(r'^delete/veichle-details/(?P<pk>.*)/$',views.delete_veichle_details),
]