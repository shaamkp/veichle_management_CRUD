from django.contrib import admin

from accounts.models import AdminProfile, SuperAdminProfile, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'username')
    exclude = ('auto_id', 'creator', 'updater', 'is_deleted', 'user')
    search_fields = ('user', )

admin.site.register(UserProfile, UserProfileAdmin)


class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'username')
    exclude = ('auto_id', 'creator', 'updater', 'is_deleted', 'user')
    search_fields = ('user', )

admin.site.register(AdminProfile, AdminProfileAdmin)


class SuperAdminProfileAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'username')
    exclude = ('auto_id', 'creator', 'updater', 'is_deleted', 'user')
    search_fields = ('user', )

admin.site.register(SuperAdminProfile, SuperAdminProfileAdmin)
