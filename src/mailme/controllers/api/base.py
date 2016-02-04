#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseAPIController(appier.Controller):

    @appier.route("/", "GET")
    def notification(self):
        return "Hello World"
