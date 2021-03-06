from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile-viewset',views.UserProfileViewset,base_name='profile-viewset')
router.register('feed',views.UserProfileFeedViewSet,base_name='profile-feed-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]