# Django-JSONEditor

Django-JSONEditor is an online structured JSON input widget for Django appropriate for various JSONField's provided for Django.

Code of the javascript JSONEditor online editor has been got from the http://jsoneditoronline.org/ but slightly changed to avoid some issues.

See the latest versions of the javascript online JSON Editor here: https://github.com/josdejong/jsoneditor

Sample views:

<img alt="json editor" src="https://raw.github.com/josdejong/jsoneditor/master/misc/jsoneditor.png">

*Don't mismatch this repo with https://github.com/skyhood/django-jsoneditor*

## Installation

    pip install "git+git://github.com/nnseva/django-jsoneditor.git"

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

* `jsoneditor.fields.django_json_field.JSONField` replaces a JSONField from https://github.com/derek-schaefer/django-json-field (**NOTE** the package is not compatible with django v.1.9)
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

## Collecting bounties

I'm collecting small bounties to integrate django-jsoneditor with different JSONField implementations, see below:

[![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264536)](https://www.bountysource.com/issues/28264536-integrate-jsoneditor-with-https-launchpad-net-django-jsonfield?utm_source=28264536&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264524)](https://www.bountysource.com/issues/28264524-integrate-jsoneditor-with-https-github-com-aychedee-unchained?utm_source=28264524&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264508)](https://www.bountysource.com/issues/28264508-integrate-jsoneditor-with-https-github-com-vialink-vlk-django-jsonfield?utm_source=28264508&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264503)](https://www.bountysource.com/issues/28264503-integrate-jsoneditor-with-https-github-com-rootbuzz-jsonate?utm_source=28264503&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264495)](https://www.bountysource.com/issues/28264495-integrate-jsoneditor-with-https-bitbucket-org-schinckel-django-jsonfield?utm_source=28264495&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264467)](https://www.bountysource.com/issues/28264467-integrate-jsoneditor-with-https-github-com-lukesneeringer-django-pgfields?utm_source=28264467&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264451)](https://www.bountysource.com/issues/28264451-integrate-jsoneditor-with-https-github-com-djangonauts-django-pgjson?utm_source=28264451&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264422)](https://www.bountysource.com/issues/28264422-integrate-jsoneditor-with-https-github-com-zacharyvoase-django-postgres?utm_source=28264422&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264409)](https://www.bountysource.com/issues/28264409-integrate-jsoneditor-with-https-github-com-djangonauts-django-rest-framework-gis?utm_source=28264409&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28264385)](https://www.bountysource.com/issues/28264385-integrate-jsoneditor-with-https-github-com-skorokithakis-django-annoying?utm_source=28264385&utm_medium=shield&utm_campaign=ISSUE_BADGE) [![Bountysource](https://api.bountysource.com/badge/issue?issue_id=35175451)](https://www.bountysource.com/issues/35175451-integrate-jsoneditor-with-new-postgresql-specific-django-jsonfield?utm_source=35175451&utm_medium=shield&utm_campaign=ISSUE_BADGE)

[![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28268324)](https://www.bountysource.com/issues/28268324-integrate-jsoneditor-with-django-suit-https-github-com-darklow-django-suit?utm_source=28268324&utm_medium=shield&utm_campaign=ISSUE_BADGE) - Django Suit integration

[![Bountysource](https://api.bountysource.com/badge/issue?issue_id=28268367)](https://www.bountysource.com/issues/28268367-integrate-jsoneditor-with-django-grappelli-https-github-com-sehmaschine-django-grappelli?utm_source=28268367&utm_medium=shield&utm_campaign=ISSUE_BADGE) - Django Grappelli integration

