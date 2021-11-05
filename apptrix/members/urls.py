from django.urls import path, include
from members.views import home_view, SignUpAPIView, MemberListAPIView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('api/clients/create', SignUpAPIView.as_view()),
    path('api/clients/auth', TokenObtainPairView.as_view()),
    path('api/list', MemberListAPIView.as_view())
]
