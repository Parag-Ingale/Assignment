from django.conf.urls import url, include, patterns
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginView, ContentView

urlpatterns = [
        url(r'^api-token-auth/', obtain_auth_token, name='api_token_auth'),
        url(r'^register/$', RegisterView.as_view(), name='register'),
        url(r'^login/$', LoginView.as_view(), name='login'),
        url(r'^create/$', ContentView.as_view(), name='create'),

]
