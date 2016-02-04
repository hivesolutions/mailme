#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import mailme

class BaseApiController(appier.Controller):

    @appier.route("/api/send", "POST", json = True)
    def send(self):
        message = mailme.Message.new()
        message.approve()
        message.send()
        return message.map()
