from django.contrib import admin

from . models import OurUsers, Friend_Requests, Message, Post, Comment
# Register your models here.

admin.site.register(OurUsers)
admin.site.register(Friend_Requests)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Comment)