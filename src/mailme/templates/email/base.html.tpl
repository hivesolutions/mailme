{% extends "email/layout.html.tpl" %}
{% block title %}Test email{% endblock %}
{% block content %}
    {{ contnts|safe }}
{% endblock %}
