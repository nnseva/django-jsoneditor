# Django-JSONEditor

Django-JSONEditor is an online structured JSON input widget for Django appropriate for various JSONField's provided for Django.

Code of the javascript JSONEditor online editor has been got from the http://jsoneditoronline.org/.

See the latest versions of the javascript online JSON Editor here: https://github.com/josdejong/jsoneditor

Sample views:

<img alt="json editor" src="https://raw.github.com/josdejong/jsoneditor/master/misc/jsoneditor.png">

*Don't mismatch this repo with https://github.com/skyhood/django-jsoneditor*

## Installation

### Latest version from the GIT repository::

    pip install "git+git://github.com/nnseva/django-jsoneditor.git"

### Stable version from the PyPi repository::

    pip install django-jsoneditor

Note that you should use one of original JSONField packages to provide the JSONField itself.

## Configuration

You **should** append `jsoneditor` into the `INSTALLED_APPS` of your `settings.py` file:
```python
INSTALLED_APPS = (
    ...
    'jsoneditor',
    ...
)
```

You **can** use CDN repositories to get JSONEditor javascript code, or host it yourself, instead of the packaged one using the following two settings in your `settings.py` file:
```python
JSON_EDITOR_JS = 'whatever-your-want.js'
JSON_EDITOR_CSS = 'whatever-your-want.css'
```

Just look to the http://cdnjs.com/libraries/jsoneditor and select the preferred one, like:
```python
JSON_EDITOR_JS = 'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/8.6.4/jsoneditor.js'
JSON_EDITOR_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/8.6.4/jsoneditor.css'
```

### Custom JSONEditor initialization
You **can** change initial parameters for the `jsoneditor.JSONEditor`
*javascript* constructor initial call for your own purposes using
`JSON_EDITOR_INIT_JS` settings. Copy the `jsoneditor/static/django-jsoneditor/init.js`
file to your own static storage, change initial values of the
`django_jsoneditor_init` object and setup the `JSON_EDITOR_INIT_JS`
variable of the `settings` file to point your own modified copy of the
file.

**Note** that the django original static file subsystem is used to
refer to the init file.

For example, let's your project has a `myapp` application,
and you would like to init all available modes of the JSONEditor
instead of two allowed by default.

* copy the `jsoneditor/static/django-jsoneditor/init.js` to `myapp/static/jsoneditor-init.js` file
* change content of the `myapp/static/jsoneditor-init.js` to:
```javascript
django_jsoneditor_init = {
    mode: 'tree',
    modes: ['code', 'form', 'text', 'tree', 'view'] // all modes
}
```
* insert into your `settings.py` file the following code:
```python
JSON_EDITOR_INIT_JS = "jsoneditor-init.js"
```
(**note** that the static file subsystem refers to static files without `static` prefix)

Also you can extend the `JSON_EDITOR_INIT_JS` file as you wish, it will be used on every
page where the `JSONEditor` widget is used just before the `django-jsonfield.js` file.

### Custom Ace initialization
In the same fashion, you can also set options for the Ace editor that is initialized when either
starting with or switching to 'code' mode. These options can be found here:
https://github.com/ajaxorg/ace/wiki/Configuring-Ace. This can for example come in handy when
wanting to customize for example the height or looks of the editor. The default of this file can be
found in `jsoneditor/static/django-jsoneditor/ace_options.js`, which is empty. A custom one can be
pointed to by adding the following line to your `settings.py`:
 ```python
JSON_EDITOR_ACE_OPTIONS_JS = "[your_ace_options_file].js"
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

Right now there are the following fixed implementations:

* `jsoneditor.fields.django_json_field.JSONField` replaces a `JSONField` from https://github.com/derek-schaefer/django-json-field (**NOTE** the package is not compatible with django v.1.9)
* `jsoneditor.fields.django_jsonfield.JSONField` replaces a `JSONField` from https://launchpad.net/django-jsonfield package
* `jsoneditor.fields.postgres_jsonfield.JSONField` replaces `django.contrib.postgres.fields.JSONField` (**NOTE** this field type appears only from django v.1.9)
* `jsoneditor.fields.django_extensions_jsonfield.JSONField` replaces `django_extensions.db.fields.json.JSONField`
* `jsoneditor.fields.jsonfield` has been added for people using https://github.com/rpkilby/jsonfield (the https://github.com/bradjasper/django-jsonfield now redirects there)
* `jsoneditor.fields.django3_jsonfield` uses the standard JSONField and JSONFormField provided by Django 3+

To use the fixed implementation instead of the original one, just replace your import with the desired one. For example, for Django 3.0 and above:

models.py:
```python
from django.db import models

# from json_field import JSONField replaced by:
from jsoneditor.fields.django3_jsonfield import JSONField
# Create your models here.

class TestModel(models.Model):
    my_field = JSONField()
```

You can access the underlying ``JSONEditor`` JS objects in your JavaScript via dictionary named ``jsonEditors``. This dictionary's keys are the IDs of the fields generated by this component in the form: ``"id"+[your form field name]+"_json_jsoneditor"``, e.g. ``id_template_parameters_json_jsoneditor``. The values in the dictionary are the instances of the correspondent JSONEditor objects.  


## Jsonschema

You can pass a jsonschema in as an arguement to `JSONEditor` widget so that
jsoneditor can validate user input. Example:

``` python
from django import forms
from jsoneditor.forms import JSONEditor

class MyAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if isinstance(field, forms.fields.JSONField):
            field.widget = JSONEditor({
                "type": "array",
                "items": {
                    "type": "string"
                }
            })
        return field

```


## Collecting bounties

You are free to give some bounties on https://www.bountysource.com/ to force solving existent or new issues
