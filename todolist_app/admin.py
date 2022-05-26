import site
from django.contrib import admin
from todolist_app.models import Contact, TaskList

# Register your models here.
admin.site.register(TaskList)
admin.site.register(Contact)
