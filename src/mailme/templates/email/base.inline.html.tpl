{% extends "email/layout.inline.html.tpl" %}
{% block title %}{{ title|default(subject, True)|default("Test email", True) }}{% endblock %}
{% block content %}
    {% block subtitle %}
        {% if subtitle %}<h2 class="subtitle">{{ subtitle }}</h2>{% endif %}
    {% endblock %}
    {% if mode == "markdown" %}
        {{ contents|markdown }}
    {% elif mode == "html" %}
        {{ contents|safe }}
    {% else %}
        {{ contents|safe }}
    {% endif %}
{% endblock %}
