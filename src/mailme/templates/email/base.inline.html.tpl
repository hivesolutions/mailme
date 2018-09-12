{% extends "email/layout.inline.html.tpl" %}
{% block title %}{{ title|default(subject, True)|default("Test email", True) }}{% endblock %}
{% block content %}
    {% if mode == "markdown" %}
        {{ contents|markdown }}
    {% elif mode == "html" %}
        {{ contents|safe }}
    {% else %}
        {{ contents|safe }}
    {% endif %}
{% endblock %}
