from django.contrib import admin

from todolist.models import Tag, Task


admin.site.register(Tag)
admin.site.register(Task)
