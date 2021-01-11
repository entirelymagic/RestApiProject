from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # no need for slash
router.register('profiles', views.UserProfileViewSet)  # no need to provide base set - because of the queryset provided

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),  # login api view
    path('', include(router.urls))
]
