from django.contrib import admin
from .models import MyUser
from .forms import MyUserCreationForm, MyUserChangeForm
# from django.conf import settings
from django.contrib.auth.models import User as Baseuser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'mobile', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'mobile', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'mobile')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

# admin.site.unregister(Baseuser)
admin.site.register(MyUser, MyUserAdmin)
