{% extends "email/layout.html.tpl" %}
{% block title %}{{ subject|default("Test email", True) }}{% endblock %}
{% block content %}
    {{ contents|safe }}
{% endblock %}
