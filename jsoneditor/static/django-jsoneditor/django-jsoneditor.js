var jsonEditors = {};

django.jQuery(function () {
    if (typeof(jsoneditor) == "undefined")
        jsoneditor = {JSONEditor: JSONEditor};
    setInterval(function () {
        var fields = django.jQuery(".for_jsoneditor");
        for (var i = 0; i < fields.length; i++) {
            var $f = django.jQuery(fields[i]);
            var id = $f.attr("id") + "_jsoneditor";
            var name = $f.attr("name") + "_jsoneditor";
            var $nxt = $f.parent().find('#' + id);
            if ($nxt.attr("name") == name) {
                continue;
            }
            var value = $f[0].value;
            var disabled = $f.is(':disabled');

            $nxt.detach();
            $nxt = django.jQuery('<div class="outer_jsoneditor" cols="40" rows="10" id="' + id + '" name="' + name + '"></div>');
            $f.parent().append($nxt);
            var fnc = function (f, nxt, value) {
                var editor = new jsoneditor.JSONEditor(nxt, Object.assign({
                    onChange: function () {
                        f.value = editor.getText();
                    },
                    // If switching to code mode, properly initialize with ace options
                    onModeChange: function(endMode, startMode) {
                        if (endMode == 'code') {
                            editor.aceEditor.setOptions(django_jsoneditor_ace_options);
                        }
                    },
                    onEditable: function() {
                        return !disabled;
                    }
                }, django_jsoneditor_init));

                // Load the editor.
                try {
                    editor.set(JSON.parse(value));
                } catch (e) {
                    // Force editor mode to "code" if there are JSON parse errors.
                    editor.setMode('code');

                    // Initialise contents of form even on unparseable JSON on load
                    editor.setText(value);
                }

                // If initialized in code mode, set ace options right away
                if (editor.mode == 'code') {
                    editor.aceEditor.setOptions(django_jsoneditor_ace_options);

                    // Format the code on first load
                    editor.format();
                }

                return editor;
            };
            jsonEditors[id] = fnc($f[0], $nxt[0], value);
        }
    }, 10);
});
