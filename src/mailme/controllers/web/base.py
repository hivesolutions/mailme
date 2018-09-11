#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseController(appier.Controller):

    @appier.route("/render", ("GET", "POST"))
    @appier.ensure(token = "admin", context = "admin")
    def render(self):
        mode = self.field("mode", "markdown")
        title = self.field("title")
        copyright = self.field("copyright")
        contents = self.field("contents", mandatory = True)
        markdown = self.field("markdown", True, cast = bool)
        return self.template(
            "email/base.html.tpl",
            mode = mode,
            title = title,
            copyright = copyright,
            contents = contents,
            markdown = markdown
        )
