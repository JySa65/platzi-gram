from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.

admin.site.unregister(User)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created_at',
        'updated_at',
    )
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields': (('created_at', 'updated_at'),),
        })
    )
    readonly_fields = ('created_at', 'updated_at')


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
