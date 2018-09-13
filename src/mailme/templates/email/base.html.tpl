{% extends "email/layout.html.tpl" %}
{% block title %}{{ title|default(subject, True)|default("Test email", True) }}{% endblock %}
{% block content %}
    {% block subtitle %}
        {% if subtitle %}{{ h2(subtitle) }}{% endif %}
    {% endblock %}
    {% if mode == "markdown" %}
        {{ contents|markdown }}
    {% elif mode == "html" %}
        {{ contents|safe }}
    {% else %}
        {{ contents|safe }}
    {% endif %}
{% endblock %}
