from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(label='Заголовок: ')
    URL = forms.CharField(label="URL: ")
    content = forms.CharField(widget=forms.Textarea, label='Контент:')
    photo = forms.ImageField(label="выберете картинку: ")
    agree = forms.BooleanField(label='Публикация')
    categories = forms.ChoiceField(choices=((1, 'Категория не выбрана'), (2, 'Новость'), (3, 'Статья')))

    # title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={'class': 'main__input'}))
    # content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'main__textarea'}))
    # is_published = forms.BooleanField(label="опубликовано", initial=True)
    # category = forms.ChoiceField(choices=((1, "Спорт"), (2, 'Красота'), (3, 'погода')), label='Категория')