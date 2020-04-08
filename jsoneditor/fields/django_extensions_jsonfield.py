from django_extensions.db.fields.json import JSONField as _JSONField
from django import forms
from django.core.exceptions import ValidationError

from jsoneditor.forms import JSONEditor

import json
import six

class JSONFormField(forms.CharField):
    widget = JSONEditor
    def __init__(self,*av,**kw):
        kw['widget'] = self.widget # force avoiding widget override
        super(JSONFormField,self).__init__(*av,**kw)

class JSONField(_JSONField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': kwargs.get('form_class', JSONFormField),
        }
        defaults.update(kwargs)
        return super(JSONField, self).formfield(**defaults)

    def to_python(self, value):
        if isinstance(value, six.string_types):
            try:
                json.loads(value)
            except json.decoder.JSONDecodeError as ex:
                raise ValidationError(ex)
        return super(JSONField, self).to_python(value)
