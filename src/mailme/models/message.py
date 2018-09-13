#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from . import base

class Message(base.MailmeBase):

    sender = appier.field()

    receivers = appier.field(
        type = list
    )

    inline = appier.field(
        type = bool,
        initial = True
    )

    style = appier.field(
        initial = "base"
    )

    mode = appier.field(
        initial = "markdown"
    )

    subject = appier.field(
        initial = "Test email"
    )

    title = appier.field()

    subtitle = appier.field()

    contents = appier.field()

    copyright = appier.field()

    logo_url = appier.field(
        meta = "url"
    )

    @classmethod
    def validate(cls):
        return super(Message, cls).validate() + [
            appier.not_null("receivers"),
            appier.not_empty("receivers")
        ]

    def send(self, owner = None):
        owner = owner or appier.get_app()

        # determines the right template so be used for the email
        # generation taking into account if this is just a test
        # email or a "real" one and if the inline engine is active
        if self.contents:
            file_name = "base.inline.html.tpl" if self.inline else "base.html.tpl"
        else:
            file_name = "test.html.tpl"

        kwargs = dict()
        if self.sender: kwargs["sender"] = self.sender

        appier_extras.admin.Base.send_email_g(
            owner,
            "email/%s" % file_name,
            receivers = self.receivers,
            inline = self.inline,
            style = self.style or "base",
            mode = self.mode or "markdown",
            subject = self.subject or "Test email",
            title = self.title or self.subject or "Test email",
            subtitle = self.subtitle,
            contents = self.contents,
            copyright = self.copyright,
            logo_url = self.logo_url or None,
            **kwargs
        )
