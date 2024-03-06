# [Mailme](http://mailme.hive.pt) 📬

Simple REST HTTP service to send emails using a simple API.

## API

## API Routes

#### GET /api/ping

```json
{
    "time" : 1455803800.5819314
}
```

#### POST /api/send

* `skey` - The secret key to be used for validation/authorization

## API Structures

#### Message

```json
{
    "receivers" : ["João Magalhães <joamag@hive.pt>", "geral@hive.pt"],
    "subject" : "Hello World subject",
    "title" : "Hello World title",
    "contents" : "This is just a random <strong>Hello World</strong> ?",
    "copyright" : "Hive Solutions"
}
```

## License

Mailme is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://github.com/hivesolutions/mailme/workflows/Main%20Workflow/badge.svg)](https://github.com/hivesolutions/mailme/actions)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/mailme/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/mailme?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/mailme.svg)](https://pypi.python.org/pypi/mailme-py)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
