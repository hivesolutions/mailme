#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from . import base

class Message(base.MailmeBase):

    sender = dict(
        type = str
        
    )
    
    receivers = dict(
        type = list
    )
    
    subject = dict(
        type = str
    )
    
    @classmethod
    def validate(cls):
        return super(Message, cls).validate() + [
            appier.not_null("receivers"),
            appier.not_empty("receivers")
        ]

    def send(self):
        base = appier_extras.admin.Base()
        base.send_email(
            "email/test.html.tpl",
            receivers = self.receivers,
            subject = self.subject or "Test email"
        )
