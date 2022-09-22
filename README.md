# restAPI

## Create document:

http://localhost:8000/api/create/

``` 
{
    "name": "El gran billete",
    "type_document": 1,
    "amount": 100,
    "typification": 1
}
```

## Get all documents:

http://localhost:8000/api/all/
``` 
[
    {
        "name": "La princesita",
        "type_document": 1,
        "amount": 10,
        "typification": 1
    },
    {
        "name": "Vendes o Vendes",
        "type_document": 2,
        "amount": 5,
        "typification": 6
    },
    {
        "name": "El gran billete",
        "type_document": 1,
        "amount": 100,
        "typification": 1
    }
]
```

## PUT one document:

http://localhost:8000/api/update/1/


``` 
{
        "name": "La princesita final",
        "type_document": 1,
        "amount": 10,
        "typification": 1
 }
```

## GET one document:

http://localhost:8000/api/document/2/detail/


``` 
{
    "name": "Vendes o Vendes",
    "type_document": 2,
    "amount": 5,
    "typification": 6
}
```

## DELETE one document:

http://localhost:8000/api/document/3/delete/

``` 
Status 202 Acepted
```
