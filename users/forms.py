from django.contrib.auth import UserCreationForm, UserChangeForm

from .models import ExtendedUser


class ExtendedUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ExtendedUser
        fields = UserCreationForm.Meta.fields


class ExtendedUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = ExtendedUser
        fields = UserChangeForm.Meta.fields
