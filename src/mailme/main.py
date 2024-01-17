#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras


class MailmeApp(appier.WebApp):
    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self, name="mailme", parts=(appier_extras.AdminPart,), *args, **kwargs
        )

    def start(self, *args, **kwargs):
        appier.WebApp.start(self, *args, **kwargs)
        self.admin_part.add_section_item("Applier", "admin.applier", section="Mailme")

    def _version(self):
        return "0.1.3"

    def _description(self):
        return "Mailme"

    def _observations(self):
        return "Simple Email Sender API"


if __name__ == "__main__":
    app = MailmeApp()
    app.serve()
else:
    __path__ = []
