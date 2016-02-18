# [Mailme](http://mailme.hive.pt)

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

* `key` - The secret key to be used for validation/authorization

## API Structures

#### Message

```json
{
    "subject" : "Hello World",
    "contents" : "This is just a random <strong>Hello World</strong> ?",
    "variables" : {
        "variable_1" : "value_1",
        "variable_2" : 12123123,
    },
    "receivers" : ["João Magalhães <joamag@gmail.com>", "geral@hive.pt"]
}
```
