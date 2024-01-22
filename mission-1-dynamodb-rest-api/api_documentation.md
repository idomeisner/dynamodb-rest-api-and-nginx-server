## API Documentation

### Table of contents
* [GET](#get)
* [PUT](#put)
<br>

**Database Type**<br>
DynamoDB

**Database tables**<br>
customer_ids

**Table keys**<br>
`id` (partition key)

**Available Methods**<br>
- GET
- PUT
<br>

## GET

Check whether a customer is in the DynamoDB table.
<br>

### Request Syntax

**Parameters:**
- `id` (string) - The customer’s ID (required)

**Return Type**<br>
dict
<br>

### Response Syntax

```json
{
    "id": "string",
    "customerInDB": "boolean",
    "message": "string"
}
```
<br>

### Response Structure
- (dict) -
  Represents the output of the GET operation.
  - `id` **(string)** - Optional\
    The checked customer’s ID.\
    The parameter exists only if the operation is successful.
  - `customerInDB` **(boolean)** - Optional\
    Indicates whether the customer is in the table.\
    The parameter exists only if the operation is successful.
  - `message` **(string)** - Optional\
    Display the error message in case the operation fails.
<br>

### Notes
- Parameters other than `id` will be ignored.
- The customer's ID has no defined structure, so any ID structure is valid.\
  The only exception are IDs containing spaces - they are not valid.
<br>

## PUT

Update the DynamoDB table with a new customer.

### Request Syntax

```json
{
    "id": "string"
}
```

**Parameters:**
- `id` (string) - The customer’s ID (required)

**Return Type**<br>
dict
<br>

### Response Syntax

```json
{
    "customer": {
        "id": "string"
    },
    "message": "string"
}
```
<br>

### Response Structure
- (dict) -
  Represents the output of the PUT operation
  - `customer` (dict) - Optional\
    The customer that was added to the DynamoDB table.\
    The parameter exists only if the operation is successful.
  - `message` (string) -\
    Display ‘success’ if the customer was successfully added to the table.\
    Display the error message in case the operation fails.
<br>

### Notes
- Parameters other than `id` will be ignored.
- The customer's ID has no defined structure, so any ID structure is valid.\
  The only exception are IDs containing spaces - they are not valid.
- There is no verification whether an ID is already in the DB.\
  If ID is already in the DB, it will be written and the operation will return ‘success’.
