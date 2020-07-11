from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import Parent, User


class SchoolSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_school = True
        if commit:
            user.save()
        return user


class ParentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.save()
        parent = Parent.objects.create(user=user)
        return user
