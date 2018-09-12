#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseController(appier.Controller):

    @appier.route("/render", ("GET", "POST"))
    @appier.ensure(token = "admin", context = "admin")
    def render(self):
        inline = self.field("inline", True, cast = bool)
        style = self.field("style", "base")
        mode = self.field("mode", "markdown")
        title = self.field("title")
        copyright = self.field("copyright")
        logo_url = self.field("logo_url")
        contents = self.field("contents", mandatory = True)
        template = "email/base.inline.html.tpl" if inline else "email/base.html.tpl"
        return self.template(
            template,
            style = style,
            mode = mode,
            title = title,
            copyright = copyright,
            logo_url = logo_url,
            contents = contents
        )
