#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class AdminController(appier.Controller):

    @appier.route("/admin/applier", "GET")
    @appier.ensure(token = "admin", context = "admin")
    def applier(self):
        mode = self.field("mode", "markdown")
        title = self.field("title")
        copyright = self.field("copyright")
        logo_url = self.field("logo_url")
        contents = self.field("contents")
        return self.template(
            "admin/applier.html.tpl",
            section = "section:mailme:applier",
            mode = mode,
            title = title,
            copyright = copyright,
            logo_url = logo_url,
            contents = contents
        )

    @appier.route("/admin/applier", "POST")
    @appier.ensure(token = "admin", context = "admin")
    def do_applier(self):
        mode = self.field("mode", "markdown")
        title = self.field("title")
        copyright = self.field("copyright")
        logo_url = self.field("logo_url")
        contents = self.field("contents", mandatory = True)
        return self.template(
            "admin/applier.html.tpl",
            section = "section:mailme:applier",
            mode = mode,
            title = title,
            copyright = copyright,
            logo_url = logo_url,
            contents = contents
        )