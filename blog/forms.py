from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from blog.models import Items
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email", "first_name", "last_name")
        field_classes = {'username': UsernameField, 'email': forms.EmailField, 'first_name': forms.CharField, 'last_name': forms.CharField}

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class BookForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('item_name', 'item_price', 'item_status', 'item_description', 'author_id',)


class CommentForm(forms.ModelForm):
    pass

class OrderForm(forms.ModelForm):
    pass