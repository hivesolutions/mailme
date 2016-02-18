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

* `skey` - The secret key to be used for validation/authorization

## API Structures

#### Message

```json
{
	"receivers" : ["João Magalhães <joamag@hive.pt>", "geral@hive.pt"],
    "subject" : "Hello World",
    "contents" : "This is just a random <strong>Hello World</strong> ?",
    "copyright" : "Hive Solutions"
}
```
