from . import views
from django.urls import path

urlpatterns = [
    path('', views.OcrimageList.as_view(), name='oc_home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
