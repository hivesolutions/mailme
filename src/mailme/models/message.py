#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from . import base

class Message(base.MailmeBase):

    sender = dict()

    receivers = dict(
        type = list
    )

    subject = dict()

    title = dict()

    contents = dict()

    copyright = dict()

    @classmethod
    def validate(cls):
        return super(Message, cls).validate() + [
            appier.not_null("receivers"),
            appier.not_empty("receivers")
        ]

    def send(self):
        file_name = "base.html.tpl" if self.contents else "test.html.tpl"
        appier_extras.admin.Base.send_email_g(
            "email/%s" % file_name,
            receivers = self.receivers,
            subject = self.subject or "Test email",
            title = self.title or self.subject or "Test email",
            contents = self.contents,
            copyright = self.copyright
        )
