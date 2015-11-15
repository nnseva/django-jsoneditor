from django.contrib import admin

from . import models
# Register your models here.

class TestAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.TestModel,TestAdmin)