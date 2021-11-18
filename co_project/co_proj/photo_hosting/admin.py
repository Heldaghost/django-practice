from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from photo_hosting.models import *

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Collections)
admin.site.register(UserProfile)
admin.site.register(Likes)
# admin.site.unregister(User)
#
#
# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#
#
# class UserProfileAdmin(UserAdmin):
#     inlines = [UserProfileInline]
#
#
# admin.site.register(User, UserProfileAdmin)
