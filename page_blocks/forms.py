from django import forms

from page_blocks.models import User


class AuthorizationForm(forms.Form):
    username = forms.CharField(label="Представьтесь", max_length=60)
    password = forms.CharField(label="Введите пароль", max_length=30, widget=forms.PasswordInput)

    def clean_user_name(self):
        data = self.cleaned_data['user_name']
        if not User.objects.filter(username=data).exists():
            raise forms.ValidationError('Пользователь не существует')
        return data


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Представьтесь", max_length=60)
    email = forms.EmailField(label="Введите ваш E-mail", max_length=30)
    password = forms.CharField(label="Введите пароль", max_length=30, widget=forms.PasswordInput)
    password_check = forms.CharField(label="Пожалуйста, повторите ваш пароль", max_length=30,
                                     widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('Пользователь с данным именем уже существует')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Введённый email уже используется')
        return data

    def clean_password_check(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_check']:
            raise forms.ValidationError('Введённые пароли не совпадают')
        return self.cleaned_data['password']


class FeedbackForm(forms.Form):
    text = forms.CharField(label="Введите текст обратной связи", max_length=1000, widget=forms.Textarea)
