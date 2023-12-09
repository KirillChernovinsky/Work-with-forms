from django.shortcuts import render
from django.http import HttpResponse

from .forms import NewsForm

load_posts = []
my_dict = {}
all_values = []
# Create your views here
def post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        URL = request.POST.get('URL')
        content = request.POST.get('content')
        photo = request.POST.get('photo')
        categories = request.POST.get('categories')
        my_dict['categories'] = categories
        my_dict['URL'] = URL
        my_dict['title'] = title
        my_dict['content'] = content
        my_dict['photo'] = photo
        load_posts.append(my_dict)
        for dictionary in load_posts:
            # Итерируемся по ключам словаря
            for value in dictionary.values():
                all_values.append(value)
        # return HttpResponse(f' {title},  {content}')
        return render(request, "app2/response.html", context={'all_values': all_values})
    else:
        form = NewsForm()
        return render(request, 'app2/index.html', context={'form': form})




