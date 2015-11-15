# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsoneditor.fields.django_json_field


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_django_json_field', jsoneditor.fields.django_json_field.JSONField(default='null', help_text=b'Test JSON editor for the django-json-field from https://github.com/derek-schaefer/django-json-field', null=True, verbose_name=b'Test JSON 1', blank=True)),
            ],
        ),
    ]
