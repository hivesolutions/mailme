{% extends "email/macros.html.tpl" %}
{% block html %}
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        {% block head %}
            <title>{% block title %}{% endblock %}</title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, minimum-scale=1, maximum-scale=1" />
        {% endblock %}
        <style type="text/css">
            {% block style %}
                {% include "styles/" + style + ".css.tpl" with context %}
            {% endblock %}
        </style>
    </head>
    <body>
        <div class="container">
            <div>
                {% if logo_url %}
                    <div class="logo-url">
                        <img src="{{ logo_url }}" alt="logo" />
                    </div>
                {% endif %}
                <div class="content">
                    <h1 class="title">{{ self.title() }}</h1>
                    {% block content %}{% endblock %}
                </div>
                <div class="footer">
                    &copy; {{ copyright|default("2014-2018 Hive Solutions", True) }} &middot; All rights reserved<br/>
                </div>
            </div>
        </div>
    </body>
    </html>
{% endblock %}
