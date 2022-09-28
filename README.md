# restAPI

## Documents
#### Create document:

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

#### Get all documents:

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
]
```

#### PUT one document:

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

#### GET one document:

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

#### DELETE one document:

http://localhost:8000/api/document/3/delete/

``` 
Status 202 Acepted
```
## Cart
### Shopping Cart endpoints

#### Get cart details 
http://localhost:8000/api/cart/cart-detail/


``` 
[
    [
        "2",
        {
            "userid": null,
            "product_id": 2,
            "name": "Vendes o Vendes",
            "quantity": 1,
            "price": "5.00"
        }
    ],
    [
        "3",
        {
            "userid": null,
            "product_id": 3,
            "name": "Los gatos felices",
            "quantity": 1,
            "price": "15.50"
        }
    ],
    [
        "1",
        {
            "userid": null,
            "product_id": 1,
            "name": "La princesita final",
            "quantity": 2,
            "price": "5.00"
        }
    ]
]
```

#### POST cart add

The id is the id of the product or document

http://localhost:8000/api/cart/add/1/

#### POST cart add

http://localhost:8000/api/cart/item_clear/1/

#### POST item increment into cart

http://localhost:8000/api/cart/item_increment/1/

#### POST item decrement into cart

http://localhost:8000/api/cart/item_decrement/1/

#### POST clear cart

http://localhost:8000/api/cart/cart_clear/