from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

#@admin.register(Profile)
#class ProfileAdmin(admin.ModelAdmin):
#    fieldsets = (
#        (None, {'fields': ('username', 'password')}),
#        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile', 'city', 'state', 'pincode', 'country')}),
#        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#        (('Status'),{'category'}),
#        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
#    )

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile', 'address', 'city', 'state', 'pincode', 'country', 'category')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

#admin.site.register(Profile)

