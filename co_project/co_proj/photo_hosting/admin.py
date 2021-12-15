from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from photo_hosting.models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at', 'collection', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'collection', 'user')
    # list_editable = ('is_published',)
    list_filter = ('collection', 'created_at')
    fields = ('title', 'content', 'user', 'created_at', 'updated_at', 'collection', 'photo', 'get_photo', 'tags')
    readonly_fields = ('user', 'get_photo', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'No photo'

    get_photo.short_description = 'Photo'


class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user')
    # list_editable = ('is_published',)
    list_filter = ('created_at',)
    fields = ('title', 'description', 'user_id', 'created_at', 'avatar', 'get_photo')
    readonly_fields = ('user_id', 'get_photo', 'created_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="75">')
        else:
            return 'No avatar'

    get_photo.short_description = 'Avatar'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    list_display_links = ('id',)
    search_fields = ('post', 'user')
    # list_editable = ('is_published',)
    list_filter = ('created_at',)
    fields = ('user', 'post', 'created_at', 'content',)
    readonly_fields = ('user', 'post', 'created_at')
    save_on_top = True


class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_display_links = ('id',)
    search_fields = ('post', 'user')
    # list_editable = ('is_published',)
    fields = ('user', 'post')
    readonly_fields = ('user', 'post')
    save_on_top = True


class FavAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'col_id')
    list_display_links = ('id',)
    search_fields = ('col_id', 'user_id')
    # list_editable = ('is_published',)
    fields = ('user_id', 'col_id')
    readonly_fields = ('user_id', 'col_id')
    save_on_top = True


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birth_date', 'get_photo')
    list_display_links = ('id',)
    search_fields = ('user',)
    # list_editable = ('is_published',)
    list_filter = ('avatar',)
    fields = ('user', 'description', 'birth_date', 'avatar', 'get_photo')
    readonly_fields = ('user', 'get_photo', 'birth_date')
    save_on_top = True

    def get_photo(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="75">')
        else:
            return 'No avatar'

    get_photo.short_description = 'Avatar'


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Collections, CollectionsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(FavCollections, FavAdmin)
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

admin.site.site_title = 'Photo hosting admin panel'
admin.site.site_header = 'Admin panel'
