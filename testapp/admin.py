from django.contrib import admin

from . import models
# Register your models here.

class TestStackedInline(admin.StackedInline):
    model = models.TestSubModel1
    extra = 1

class TestTabularInline(admin.StackedInline):
    model = models.TestSubModel2
    extra = 1

class TestAdmin(admin.ModelAdmin):
    inlines = (
            TestStackedInline,
            TestTabularInline
    )
    pass

admin.site.register(models.TestModel,TestAdmin)