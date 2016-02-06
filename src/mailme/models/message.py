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

    contents = dict()

    @classmethod
    def validate(cls):
        return super(Message, cls).validate() + [
            appier.not_null("receivers"),
            appier.not_empty("receivers")
        ]

    def send(self):
        base = appier_extras.admin.Base()
        file_name = "base.html.tpl" if self.contents else "test.html.tpl"
        base.send_email(
            "email/%s.html.tpl" % file_name,
            receivers = self.receivers,
            subject = self.subject or "Test email",
            contents = self.contents
        )
