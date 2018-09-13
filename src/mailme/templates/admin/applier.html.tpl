{% extends "admin/admin.fluid.html.tpl" %}
{% block title %}Applier{% endblock %}
{% block name %}Applier{% endblock %}
{% block content %}
    {% if contents %}
        {% set url = url_for(
            "base.render",
            mode = mode,
            style = style,
            title = title,
            subtitle = subtitle,
            copyright = copyright,
            logo_url = logo_url,
            contents = contents
        ) %}
        {% set url_absolute = url_for(
            "base.render",
            mode = mode,
            style = style,
            title = title,
            subtitle = subtitle,
            copyright = copyright,
            logo_url = logo_url,
            contents = contents,
            absolute = True
        ) %}
    {% endif %}
    <form action="{{ url_for('admin.do_applier') }}" method="post" class="form">
        <div class="label">
            <label>Style</label>
        </div>
        <div class="input">
             <input name="style" type="text" class="text-field" value="{{ style|default('base', True) }}" />
        </div>
        <div class="label">
            <label>Title</label>
        </div>
        <div class="input">
             <input name="title" type="text" class="text-field" value="{{ title|default('', True) }}" />
        </div>
        <div class="label">
            <label>Sub-Title</label>
        </div>
        <div class="input">
             <input name="subtitle" type="text" class="text-field" value="{{ subtitle|default('', True) }}" />
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
        <div class="buttons">
            <span class="button button-color button-green" data-submit="true">Generate HTML</span>
            {% if contents %}
                <span class="or">or</span>
                <a class="button button-color button-grey"
                   href="{{ url_absolute }}" target="_blank">Open URL</a>
            {% endif %}
        </div>
    </form>
    {% if contents %}
        <div class="input">
            <iframe src="{{ url }}" style="width: 100%;height: 800px;border: none;box-sizing: border-box;"></iframe>
        </div>
    {% endif %}
{% endblock %}
