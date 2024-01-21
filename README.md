## Background
This repository is an assignment I received and my solution.\
The assignment check for basic AWS knowledge.
<br><br>

## Assignment

**Prerequisite knowledge**

- Python
- AWS Services
  - Lambda
  - API Gateway
  - Dynamo DB
  - IAM
  - EC2
<br>

**Important notes**

Please read the following instructions before starting the implementation. \
Keep your code clean and clear.
<br>

### Mission 1 - DynamoDB REST API

**The Scenario**

The backend development team requests you to develop a REST API that will be responsible for storing the product user’s IDs.\
Of course, don’t forget to write down API documentation or a README file that will give specific instructions for the Backend team.
<br>

**REST API methods**

1. `PUT` – Insert a new ID into the company Dynamo DB table.
2. `GET` – Create the proper lambda function to handle get requests from the server and return a simple JSON response that will indicate whether the ID is in the DB.
<br>

**Naming Convention**

- DynamoDB Table Name - `customer_ids`
- Lambda function/s – _Python_ - Function names should be lowercase, with words separated by underscores.
<br>

### Mission 2 - Setting Up NGINX Server

Please deploy a static website using a NGINX server on an Ubuntu machine using AWS.

**! Open this server only to IP xxx.xxx.xxx.xxx over HTTP !**

**AMI -** Ubuntu Server 20.04 LTS (HVM), SSD Volume Type

**Instance Type -** t2.micro

**HTML Template:**

```html
<!doctype html>
<html>
   <head>
      <meta charset="utf-8">
      <title>NGINX Server</title>
   </head>
   <body>
      <h1>Hello from the NGINX Server</h1>
      <p>Congratulations!</p>
   </body>
</html>
```
<br>

**Once you are finished, please provide us with a link to this static page and IAM user to connect to your AWS environment.**

Good luck
