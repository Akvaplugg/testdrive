from django import forms

CARS = ((1, "Nissan Murano"), (2, "ВАЗ 2114"), (3, "Vivo V12"))
class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = forms.CharField(label='Телефон')
    email = forms.CharField(label='Почта')
    car = forms.ChoiceField(label='Авто', choices=CARS)
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)
