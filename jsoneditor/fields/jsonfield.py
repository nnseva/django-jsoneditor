from jsonfield import JSONField as _JSONField
from jsonfield.fields import JSONCharField as _JSONFormField

from jsoneditor.forms import JSONEditor

class JSONFormField(_JSONFormField):
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
