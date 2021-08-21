## WAFI API Interview Question

POST - ```/user/register```

Payload
```js
{
    "primaryKey": "email@domain.com",
    "secondaryKey": "A"
}
```

PUT - `/app/deposit`

Payload
```js
{
    "primaryKey": "email@domain.com",
    "secondaryKey": "A",
    "balance": 10
}
```

GET - `/app/balance`

Response
```js
{
    "primaryKey": "email@domain.com",
    "secondaryKey": "A",
    "balance": 10
    ........
}
```

POST - `/app/send`

Payload
```js
{
    "senderId": "email@domain.com",
    "destinationId": "email@domain.com",
    "balance": 10
    ........
}
```

POST - `/app/source`

Payload
```js
{
    "senderId": "email@domain.com",
    "destinationId": "ABSA",
    "balance": 10
    ........
}
```