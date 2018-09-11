{% extends "admin/admin.fluid.html.tpl" %}
{% block title %}Email Applier{% endblock %}
{% block name %}Email Applier{% endblock %}
{% block content %}
    <form action="{{ url_for('admin.do_applier') }}" method="post" class="form">
        <div class="label">
            <label>Title</label>
        </div>
        <div class="input">
             <input name="title" type="text" class="text-field" value="{{ title|default('', True) }}" />
        </div>
        <div class="label">
            <label>Copyright</label>
        </div>
        <div class="input">
             <input name="copyright" type="text" class="text-field" value="{{ copyright|default('', True) }}" />
        </div>
        <div class="label">
            <label>Logo URL</label>
        </div>
        <div class="input">
             <input name="logo_url" type="text" class="text-field" value="{{ logo_url|default('', True) }}" />
        </div>
        <div class="label">
            <label>Contents</label>
        </div>
        <div class="input">
            <textarea name="contents" class="text-area">{{ contents|default("", True) }}</textarea>
        </div>
        <div class="label">
            <label>Mode</label>
        </div>
        <div class="input">
            <div class="drop-field drop-field-select">
                <input type="hidden" name="mode" class="hidden-field" value="{{ mode|default('markdown', True) }}" />
                <ul class="data-source" data-type="local">
                    <li>
                        <span name="name">Markdown</span>
                        <span name="value">markdown</span>
                    </li>
                    <li>
                        <span name="name">HTML</span>
                        <span name="value">html</span>
                    </li>
                </ul>
            </div>
        </div>
        <span class="button" data-submit="true">Submit Options</span>
    </form>
    {% if contents %}
        <div class="input">
            {% set url = url_for(
                "base.render",
                mode = mode,
                title = title,
                copyright = copyright,
                logo_url = logo_url,
                contents = contents
            ) %}
            {% set url_absolute = url_for(
                "base.render",
                mode = mode,
                title = title,
                copyright = copyright,
                logo_url = logo_url,
                contents = contents,
                absolute = True
            ) %}
            <div class="url">
                <a href="{{ url_absolute }}" target="_blank">{{ url_absolute }}</a>
            </div>
            <iframe src="{{ url }}" style="width: 100%;height: 800px;border: none;box-sizing: border-box;"></iframe>
        </div>
    {% endif %}
{% endblock %}
