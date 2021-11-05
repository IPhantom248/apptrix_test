from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters import rest_framework as filters

from members.models import Member
from members.serializer import MemberSerializer, MemberListSerializer


def home_view(request):
    return render(request, 'home_page.html')


class SignUpAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = MemberSerializer

    def post(self, request):
        member = request.data
        serializer = self.serializer_class(data=member)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = {
            'message': 'Вы успешно зарегистрировались',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response, status=status.HTTP_201_CREATED)


class MemberFilter(filters.FilterSet):

    class Meta:
        model = Member
        fields = ['gender', 'first_name', 'last_name']


class MemberListAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MemberFilter



