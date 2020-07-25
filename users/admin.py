from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ExtendedUserCreationForm, ExtendedUserChangeForm
from .models import ExtendedUser


class ExtendedUserAdmin(UserAdmin):
    add_form = ExtendedUserCreationForm
    form = ExtendedUserChangeForm
    model = ExtendedUser


admin.site.register(ExtendedUser, ExtendedUserAdmin)
