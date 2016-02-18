#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier

import mailme

class BaseApiController(appier.Controller):

    @appier.route("/api/ping", "GET", json = True)
    def ping(self):
        return dict(
            time = time.time()
        )

    @appier.route("/api/send", "POST", json = True)
    @appier.ensure(token = "admin")
    def send(self):
        message = mailme.Message.new()
        message.approve()
        message.send()
        return message.map()
