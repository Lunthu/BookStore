from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from blog.models import Items, Orders, Comments
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_text',)

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        if commit:
            comment.save()
        return comment


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('order_adress', 'order_comment')

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        if commit:
            order.save()
        return order