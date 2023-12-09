from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm, NewsForm


# Create your views here.

# Дает возможность в index.html при команде {{ form }} создать формочки
def index(request):
    #Условный рендор
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'User {name}, Age {age}')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})


def myForm(request):
    return render(request, 'app/form.html')







def news(request):
    #Условный рендор
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        category = request.POST.get('category')
        return HttpResponse(f'Новость {title} <br>'
                            f'контент {content} <br>'
                            f'Категоря {category}, {is_published}'
                            )

    else:
        formNews= NewsForm()
        return render(request, 'app/index.html', context={'form': formNews})

# def user(request):
#     name = request.POST.get('name')
#     age = request.POST.get('age')
#     return HttpResponse(f'User {name}, Age {age}')