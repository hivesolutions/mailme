#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

import appier

import mailme


class APITest(unittest.TestCase):

    def setUp(self):
        self.app = mailme.MailmeApp(level=logging.ERROR)
        self.controller = self.app.get_controller("BaseAPIController")

    def tearDown(self):
        self.app.unload()

    def test_send(self):
        request = appier.Request("POST", "/api/send", session_c=appier.MemorySession)
        request.load_data()
        request.load_form()
        self.app._request = request

        with self.assertRaises(appier.AppierException) as context:
            self.controller.send(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "User not authenticated")

        request.session["username"] = "mailme"

        request.session["tokens"] = ["mailme.send"]
        self.assertRaises(
            appier.ValidationError, lambda: self.controller.send(request=request)
        )

        request.session["tokens"] = ["mailme.*"]
        self.assertRaises(
            appier.ValidationError, lambda: self.controller.send(request=request)
        )

        request.session["tokens"] = ["*"]
        self.assertRaises(
            appier.ValidationError, lambda: self.controller.send(request=request)
        )

        request.session["tokens"] = ["admin"]
        with self.assertRaises(appier.AppierException) as context:
            self.controller.send(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")

        request.session["tokens"] = ["mailme"]
        with self.assertRaises(appier.AppierException) as context:
            self.controller.send(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")

        request.session["tokens"] = ["mailme.to_json"]
        with self.assertRaises(appier.AppierException) as context:
            self.controller.send(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")

        request.session["tokens"] = []
        with self.assertRaises(appier.AppierException) as context:
            self.controller.send(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")

    def test_to_json(self):
        request = appier.Request("GET", "/api/to_json", session_c=appier.MemorySession)
        request.set_params(dict(contents=["Hello world"]))
        self.app._request = request

        with self.assertRaises(appier.AppierException) as context:
            self.controller.to_json(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "User not authenticated")

        request.session["username"] = "mailme"

        request.session["tokens"] = ["mailme.send"]
        result = self.controller.to_json(request=request)
        self.assertEqual(
            result, dict(contents="Hello world", mode="markdown", style="base")
        )

        request.session["tokens"] = ["*"]
        result = self.controller.to_json(request=request)
        self.assertEqual(
            result, dict(contents="Hello world", mode="markdown", style="base")
        )

        request.set_params(
            dict(
                contents=["Hello world"],
                sender=["mailme@bemisc.com"],
                receivers=["john@doe.com", "jane@doe.com"],
                mode=["html"],
                title=["Hello"],
                subtitle=[""],
            )
        )
        result = self.controller.to_json(request=request)
        self.assertEqual(
            result,
            dict(
                contents="Hello world",
                sender="mailme@bemisc.com",
                receivers=["john@doe.com", "jane@doe.com"],
                mode="html",
                style="base",
                title="Hello",
            ),
        )

        request = appier.Request("GET", "/api/to_json", session_c=appier.MemorySession)
        request.set_params(
            dict(
                contents=["Hello world"],
                sender=["mailme@bemisc.com"],
                receivers=["john@doe.com", "jane@doe.com"],
                mode=["html"],
                title=["Hello"],
                style=["simple"],
                style_css=["body { color: red; }"],
                attachments=["https://bemisc.com/file.pdf"],
                subtitle=["World"],
                copyright=["Hive Solutions"],
                logo_url=["https://bemisc.com/logo.png"],
            )
        )
        request.session["username"] = "mailme"
        request.session["tokens"] = ["mailme.send"]
        self.app._request = request
        result = self.controller.to_json(request=request)
        self.assertEqual(
            result,
            dict(
                contents="Hello world",
                sender="mailme@bemisc.com",
                receivers=["john@doe.com", "jane@doe.com"],
                mode="html",
                style="simple",
                style_css="body { color: red; }",
                attachments=["https://bemisc.com/file.pdf"],
                title="Hello",
                subtitle="World",
                copyright="Hive Solutions",
                logo_url="https://bemisc.com/logo.png",
            ),
        )

        request = appier.Request("GET", "/api/to_json", session_c=appier.MemorySession)
        request.set_params(dict(title=["Hello"]))
        request.session["username"] = "mailme"
        request.session["tokens"] = ["mailme.send"]
        self.app._request = request
        self.assertRaises(
            appier.OperationalError, lambda: self.controller.to_json(request=request)
        )

        request.set_params(dict(contents=["Hello world"]))

        request.session["tokens"] = ["admin"]
        with self.assertRaises(appier.AppierException) as context:
            self.controller.to_json(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")

        request.session["tokens"] = ["mailme"]
        with self.assertRaises(appier.AppierException) as context:
            self.controller.to_json(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")

        request.session["tokens"] = []
        with self.assertRaises(appier.AppierException) as context:
            self.controller.to_json(request=request)
        self.assertEqual(context.exception.code, 403)
        self.assertEqual(context.exception.message, "Not enough permissions")
