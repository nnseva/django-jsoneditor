from django.forms.widgets import Textarea
try:
    from django.forms.util import flatatt
except ImportError:
    from django.forms.utils import flatatt

from django.utils.safestring import mark_safe

from django.conf import settings

import json

try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring


class JSONEditor(Textarea):
    class Media:
        js = (
            getattr(settings,"JSON_EDITOR_JS",settings.STATIC_URL+'jsoneditor/jsoneditor.js'),
            settings.STATIC_URL+'django-jsoneditor/django-jsoneditor.js',
        )
        css= {'all': ( getattr(settings, "JSON_EDITOR_CSS",settings.STATIC_URL+'jsoneditor/jsoneditor.css'),)}

    def render(self, name, value, attrs=None):
        if not isinstance(value,basestring):
           value = json.dumps(value)
        input_attrs = {'hidden':True}
        input_attrs.update(attrs)
        if not 'class' in input_attrs:
            input_attrs['class'] = 'for_jsoneditor'
        else:
            input_attrs['class'] += ' for_jsoneditor'
        r = super(JSONEditor,self).render(name, value, input_attrs)
        div_attrs = {}
        div_attrs.update(attrs)
        div_attrs.update({'id':(attrs['id']+'_jsoneditor')})
        final_attrs = self.build_attrs(div_attrs, name=name)
        r += '''
        <div %(attrs)s></div>
        ''' % {
            'attrs':flatatt(final_attrs),
        }
        return mark_safe(r)
