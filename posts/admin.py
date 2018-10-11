# Django
from django.contrib import admin

# Models
from posts.models import Post

""" POST ADMIN """


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title', 'photo')

    fieldsets = (
        ('Create Post', {
            "fields": (('user', 'profile', 'title', 'photo'),),
        }),
        ('Metadata', {
            "fields": ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')
