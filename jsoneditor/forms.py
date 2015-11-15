from django.forms.widgets import Textarea
from django.forms.util import flatatt

from django.utils.safestring import mark_safe

from django.conf import settings

class JSONEditor(Textarea):
    class Media:
        js = ( getattr(settings,"JSON_EDITOR_JS",settings.STATIC_URL+'jsoneditor/jsoneditor.js'), )
        css= {'all': ( getattr(settings, "JSON_EDITOR_CSS",settings.STATIC_URL+'jsoneditor/jsoneditor.css'),)}

    def render(self, name, value, attrs=None):
        input_attrs = {'hidden':True}
        input_attrs.update(attrs)
        r = super(JSONEditor,self).render(name, value, input_attrs)
        div_attrs = {}
        div_attrs.update(attrs)
        div_attrs.update({'id':(attrs['id']+'_jsoneditor')})
        final_attrs = self.build_attrs(div_attrs, name=name)
        r += '''
        <div %(attrs)s></div>
        <script type="text/javascript">
        django.jQuery(function() {
            if( typeof(jsoneditor) == "undefined" )
                jsoneditor = { JSONEditor:JSONEditor };
            var editor_%(editor_id)s = new jsoneditor.JSONEditor(django.jQuery('#%(id)s_jsoneditor')[0],{
                    change:function() {
                        django.jQuery('#%(id)s')[0].value = JSON.stringify(editor_%(editor_id)s.get());
                    },
                },JSON.parse(django.jQuery('#%(id)s')[0].value));
            django.jQuery('#%(id)s').hide();
        });
        </script>
        ''' % {
            'attrs':flatatt(final_attrs),
            'editor_id':attrs['id'].replace('-','_'),
            'id':attrs['id'],
        }
        return mark_safe(r)
