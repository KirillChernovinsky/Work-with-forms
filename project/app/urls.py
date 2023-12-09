from django.urls import path
from .views import index, myForm, news

urlpatterns = [
    path('', index, name='home'),
    path("myform", myForm, name='form'),
    path('news', news, name='news'),
    # path('user', user, name='user')
]