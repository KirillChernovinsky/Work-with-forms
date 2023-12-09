from django import forms

class UserForm(forms.Form):
    # Charfiel отпределять input типа text (для имени)
    name = forms.CharField(max_length=20, min_length=2, initial="Kirill")
    # IntegerField отпределять input типа int (для возврастат)
    age = forms.IntegerField(max_value=10)
    agree = forms.BooleanField(label='Согласен на обработку данных')
    email = forms.EmailField()
    url = forms.URLField(required=False) #необязательно для заполнения
    file = forms.FileField()
    photo = forms.ImageField()
    date = forms.DateTimeField()
    lenguages = forms.ChoiceField(choices=((1, 'Python'), (2, 'Java'), (3, 'C'))) # параметры на выбор
    lenguages2 = forms.MultipleChoiceField(choices=((1, 'Python'), (2, 'Java'), (3, 'C'))) # можно выбрать несколько вариков
    comment = forms.CharField()
    comment2 = forms.CharField(widget=forms.Textarea, label='комментарий')# могу сделать как поле - text ara
    field_order = ['comment']



class NewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={'class': 'main__input'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'main__textarea'}))
    is_published = forms.BooleanField(label="опубликовано", initial=True)
    category = forms.ChoiceField(choices=((1, "Спорт"), (2, 'Красота'), (3, 'погода')), label='Категория')



























