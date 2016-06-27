from django.db import models

#from jsoneditor.fields.django_json_field import JSONField as JSONField1
from jsoneditor.fields.django_jsonfield import JSONField as JSONField2
# Create your models here.

class TestModel(models.Model):
#    test_django_json_field = JSONField1(verbose_name="Test JSON 1",null=True,blank=True,help_text="Test JSON editor for the django-json-field from https://github.com/derek-schaefer/django-json-field")
    test_django_jsonfield = JSONField2(verbose_name="Test JSON 2",null=True,blank=True,help_text="Test JSON editor for the django-jsonfield from https://github.com/bradjasper/django-jsonfield")

class TestSubModel1(models.Model):
    par = models.ForeignKey(TestModel)
    test_inline_json_field = JSONField2(verbose_name="Test JSON 2",null=True,blank=True,help_text="Test JSON editor for the django-jsonfield from https://github.com/bradjasper/django-jsonfield")

class TestSubModel2(models.Model):
    par = models.ForeignKey(TestModel)
    test_inline_json_field = JSONField2(verbose_name="Test JSON 2",null=True,blank=True,help_text="Test JSON editor for the django-jsonfield from https://github.com/bradjasper/django-jsonfield")
