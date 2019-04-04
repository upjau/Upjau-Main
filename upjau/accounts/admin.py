from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile
from .forms import ProfileForm

#class ProfileUserAdmin(UserAdmin):
#    add_form = ProfileForm
#    model = Profile
#    list_display = ['email', 'username']

# Inline Properties
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    #verbose_name_plural = 'Profile'
    
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(Profile)
admin.site.site_header = 'Upjau'
