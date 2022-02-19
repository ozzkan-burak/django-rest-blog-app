from xml.etree.ElementTree import Comment
from django.contrib import admin
from comment.models import Comment

# Register your models here.
admin.site.register(Comment)