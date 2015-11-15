from django.db import models

from jsoneditor.fields.django_json_field import JSONField as JSONField1
# Create your models here.

class TestModel(models.Model):
    test_django_json_field = JSONField1(verbose_name="Test JSON 1",null=True,blank=True,help_text="Test JSON editor for the django-json-field from https://github.com/derek-schaefer/django-json-field")
