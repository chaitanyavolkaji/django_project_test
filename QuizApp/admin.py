from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Quiz)
admin.site.register(models.Question)
admin.site.register(models.Answer)
