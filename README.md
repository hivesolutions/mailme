# [Mailme 📬](http://mailme.hive.pt)

**Mailme is a powerful and simple REST HTTP service that acts as an email gateway, allowing programmatic sending of emails through an easy-to-use API.** Whether you're automating workflows, sending notifications, or delivering personalized messages, Mailme provides the tools you need for efficient and reliable email communication.

## Description

Mailme is a lightweight and versatile email gateway designed to simplify the process of sending emails programmatically. Built as a RESTful HTTP service, it offers a clean and intuitive API for developers to integrate email functionality into their applications with minimal effort. 

This service is particularly useful for automated workflows, such as sending invoices, notifications, and other email-based communications. Mailme ensures flexibility by supporting multiple recipients, custom subject lines, rich HTML content, and personalization options. 

By offloading email handling to a dedicated gateway, Mailme helps developers focus on core application logic while providing reliable email delivery. Its extensible architecture and simple configuration make it an excellent choice for businesses and projects of all sizes.

### Key Features

- **Simple REST API**: Easy-to-use endpoints for sending emails and testing service availability.
- **Rich Content Support**: Send plain text, HTML, or mixed content emails with embedded formatting.
- **Multi-Recipient Capability**: Support for multiple recipients, including personalized "to", "cc" and "bcc" fields.
- **Security**: Includes secret key validation to ensure authorized access.
- **Customizable Templates**: Define subject lines, titles, and other dynamic email components.
- **Open Source**: Fully open-sourced under the Apache License 2.0, allowing for community contributions and modifications.

Mailme seamlessly integrates into existing systems and workflows, making it a go-to solution for developers in need of an efficient and reliable email gateway.

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
