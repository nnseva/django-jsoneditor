# Django-JSONEditor

Django-JSONEditor is an online structured JSON input widget for Django appropriate for various JSONField's provided for Django.

Code of the javascript JSONEditor online editor has been got from the http://jsoneditoronline.org/ but slightly changed to avoid some issues.

See the latest versions of the javascript online JSON Editor here: https://github.com/josdejong/jsoneditor

Sample views:

<img alt="json editor" src="https://raw.github.com/josdejong/jsoneditor/master/misc/jsoneditor.png">

*Don't mismatch this repo with https://github.com/bradjasper/django-jsonfield*

## Installation

    pip install "git+git:github.com/nnseva/django-jsoneditor"

Note that you should use one of original JSONField packages to provide the JSONField itself.

## Configuration

You can use CDN repositories to get JSONEditor javascript code, or host it yourself using the following two settings
in your `settings.py` file:
```python
JSON_EDITOR_JS = 'whatever-your-want.js'
JSON_EDITOR_CSS = 'whatever-your-want.css'
```

Just look to the http://cdnjs.com/libraries/jsoneditor and select the latest one, like:
```python
JSON_EDITOR_JS = 'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/4.2.1/jsoneditor.js'
JSON_EDITOR_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/4.2.1/jsoneditor.css'
```

## Use

You can use the JSONEditor widget for fields in selected Admin classes like:

admin.py:
```python
from json_field import JSONField
from jsoneditor.forms import JSONEditor
class MyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField:{ 'widget':JSONEditor },
    }
```

Or use the original JSONField implementation fixed by the package.

Right now there are two fixed implementations:

* `jsoneditor.fields.django_json_field.JSONField` replaces a JSONField from https://github.com/derek-schaefer/django-json-field
* `jsoneditor.fields.django_jsonfield.JSONField` replaces a JSONField from https://github.com/bradjasper/django-jsonfield

Use the fixed implementation instead of the original one

models.py:
```python
from django.db import models

# from json_field import JSONField replaced by:
from jsoneditor.fields.django_json_field import JSONField
# Create your models here.

class TestModel(models.Model):
    my_field = JSONField()
```
