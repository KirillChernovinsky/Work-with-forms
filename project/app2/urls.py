from django.urls import path
from .views import post

urlpatterns = [
    # path('', index, name='home'),
    path("post", post, name='post'),
    # path('news', news, name='news'),
    # # path('user', user, name='user')
]