import json
from packaging import version

import django
from django.conf import settings
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe


try:
    from django.forms.util import flatatt
except ImportError:
    from django.forms.utils import flatatt

try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str, bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring


class JSONEditor(Textarea):
    class Media:
        js = (
            'admin/js/vendor/jquery/jquery.js',
            'admin/js/jquery.init.js',
            getattr(settings, "JSON_EDITOR_JS", 'jsoneditor/jsoneditor.js'),
            getattr(settings, "JSON_EDITOR_ACE_OPTIONS_JS", 'django-jsoneditor/ace_options.js'),
            getattr(settings, "JSON_EDITOR_INIT_JS", 'django-jsoneditor/init.js'),
            'django-jsoneditor/django-jsoneditor.js',
        )
        css = {
            'all': (
                getattr(settings, "JSON_EDITOR_CSS", 'jsoneditor/jsoneditor.css'),
                'django-jsoneditor/django-jsoneditor.css',
            )
        }


    def render(self, name, value, attrs=None, renderer=None):
        if not isinstance(value, basestring):
            value = json.dumps(value)
        input_attrs = {'hidden': True}
        input_attrs.update(attrs)
        if 'class' not in input_attrs:
            input_attrs['class'] = 'for_jsoneditor'
        else:
            input_attrs['class'] += ' for_jsoneditor'
        r = super(JSONEditor, self).render(name, value, input_attrs)
        div_attrs = {}
        div_attrs.update(attrs)
        div_attrs.update({'id': (attrs['id'] + '_jsoneditor')})
        if version.parse(django.get_version()) >= version.parse("1.11"):
            final_attrs = self.build_attrs(div_attrs, extra_attrs={'name': name})
        else:
            final_attrs = self.build_attrs(div_attrs, name=name)
        r += '''
        <div %(attrs)s></div>
        ''' % {
            'attrs': flatatt(final_attrs),
        }
        return mark_safe(r)
