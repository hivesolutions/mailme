#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier

import mailme

class BaseAPIController(appier.Controller):

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

    @appier.route("/api/to_json", ("GET", "POST"), json = True)
    @appier.ensure(token = "admin")
    def to_json(self):
        sender = self.field("sender")
        receivers = self.field("receivers", cast = list)
        mode = self.field("mode", "markdown")
        style = self.field("style", "base")
        attachments = self.field("attachments", [], cast = list)
        title = self.field("title")
        subtitle = self.field("subtitle")
        copyright = self.field("copyright")
        logo_url = self.field("logo_url")
        contents = self.field("contents", mandatory = True)
        data = dict(contents = contents)
        if sender: data["sender"] = sender
        if receivers: data["receivers"] = receivers
        if mode: data["mode"] = mode
        if style: data["style"] = style
        if attachments: data["attachments"] = attachments
        if title: data["title"] = title
        if subtitle: data["subtitle"] = subtitle
        if copyright: data["copyright"] = copyright
        if logo_url: data["logo_url"] = logo_url
        return data
