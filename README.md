# Django-JSONEditor

Django-JSONEditor is an online structured JSON input widget for Django appropriate for various JSONField's provided for Django.

Code of the javascript JSONEditor online editor has been got from the http://jsoneditoronline.org/ but slightly changed to avoid some issues.

See the latest versions of the JSON Editor javascript here: https://github.com/josdejong/jsoneditor

*Don't mismatch this repo with https://github.com/bradjasper/django-jsonfield*

## Installation

    pip install "git+git:github.com/nnseva/django-jsoneditor"

## Configuration

You can use CDN repositories to get JSONEditor javascript code, or host it yourself using the following two settings
in your `settings.py` file:

    JSON_EDITOR_JS = 'whatever-your-want.js'
    JSON_EDITOR_CSS = 'whatever-your-want.css'

Just look to the http://cdnjs.com/libraries/jsoneditor and select the latest one, like:

    JSON_EDITOR_JS = 'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/4.2.1/jsoneditor.js'
    JSON_EDITOR_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/4.2.1/jsoneditor.css'

## Use

You can use the JSONEditor widget for fields in selected Admin classes like:

admin.py:

    from json_field import JSONField
    from jsoneditor.forms import JSONEditor
    class MyAdmin(admin.ModelAdmin):
        formfield_overrides = {
            JSONField:{ 'widget':JSONEditor },
        }

Use the original JSONField implementation fixed by the package:

models.py:

    from django.db import models

    from jsoneditor.fields.django_json_field import JSONField
    # Create your models here.

    class TestModel(models.Model):
        my_field = JSONField()
