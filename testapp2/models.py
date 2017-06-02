from django.db import models

from jsoneditor.fields.postgres_jsonfield import JSONField
# Create your models here.

class TestModel(models.Model):
    test_django_jsonfield = JSONField(verbose_name="Test JSON",null=True,blank=True,help_text="Test JSON editor for the django postgres-specific JSONField")

class TestSubModel1(models.Model):
    par = models.ForeignKey(TestModel)
    test_inline_json_field = JSONField(verbose_name="Test JSON",null=True,blank=True,help_text="Test JSON editor for the django postgres-specific JSONField")

class TestSubModel2(models.Model):
    par = models.ForeignKey(TestModel)
    test_inline_json_field = JSONField(verbose_name="Test JSON",null=True,blank=True,help_text="Test JSON editor for the django postgres-specific JSONField")
