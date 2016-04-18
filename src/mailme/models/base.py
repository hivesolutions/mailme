#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class MailmeBase(appier.LocalModel):

    id = appier.field(
        type = int
    )
