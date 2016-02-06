{% extends "email/layout.html.tpl" %}
{% block title %}{{ title }}{% endblock %}
{% block content %}
    {{ contnts|safe }}
{% endblock %}
