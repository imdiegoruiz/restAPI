# restAPI

## Create document:

http://localhost:8000/api/create/

``` 
{
    "name": "El gran billete",
    "type_document": 1,
    "amount": 100,
    "typification": 1,
    "price": 10.0
}
```

## Get all documents:

http://localhost:8000/api/all/
``` 
[
    {
        "id": 1,
        "name": "La princesita final",
        "type_document": 1,
        "amount": 10,
        "typification": 1,
        "price": "5.00",
        "created_at": "2022-09-23T01:55:46.683327Z",
        "updated_at": "2022-09-23T01:55:46.693576Z"
    },
    {
        "id": 2,
        "name": "Vendes o Vendes",
        "type_document": 2,
        "amount": 5,
        "typification": 6,
        "price": "5.00",
        "created_at": "2022-09-23T01:55:46.683327Z",
        "updated_at": "2022-09-23T01:55:46.693576Z"
    },
    {
        "id": 3,
        "name": "Los gatos felices",
        "type_document": 1,
        "amount": 10,
        "typification": 1,
        "price": "15.50",
        "created_at": "2022-09-23T01:59:48.252288Z",
        "updated_at": "2022-09-23T01:59:48.252580Z"
    }
]```

## PUT one document:

http://localhost:8000/api/update/1/


``` 
{
        "name": "La princesita final",
        "type_document": 1,
        "amount": 10,
        "typification": 1,
        "price":10
 }
```

## GET one document:

http://localhost:8000/api/document/2/detail/


``` 
{
        "id": 2,
        "name": "Vendes o Vendes",
        "type_document": 2,
        "amount": 5,
        "typification": 6,
        "price": "5.00",
        "created_at": "2022-09-23T01:55:46.683327Z",
        "updated_at": "2022-09-23T01:55:46.693576Z"
    }
```

## DELETE one document:

http://localhost:8000/api/document/3/delete/

``` 
Status 202 Acepted
```
