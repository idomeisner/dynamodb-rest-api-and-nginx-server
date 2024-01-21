import json
import logging
from http import HTTPStatus
from typing import Any, Dict, Optional

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TABLE_NAME = "customer_ids"
table = boto3.resource('dynamodb').Table(TABLE_NAME)


class QueryStringsError(Exception):
    pass


def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    def check_customer() -> Dict[str, Any]:
        """
        Check if a specific customer is in the DynamoDB table
        """

        try:
            # Getting the customer ID from the query string
            query_param = event['queryStringParameters'] or {}
            customer_id = query_param.get('customer_id')

            # Checking customer_id validation
            if msg := is_valid_id(customer_id):
                raise QueryStringsError(msg)

            customer = {
                'customer_id': customer_id
            }

            # Getting an item from the DynamoDB table
            response = table.get_item(
                Key={
                    'customer_id': customer_id
                }
            )

            body = {
                'customer_id': customer_id,
                'customerInDB': "Item" in response
            }

            return build_response(HTTPStatus.OK, body)

        except Exception as e:
            body = {
                'message': f"{type(e).__name__}: {e}"
            }
            logger.error(f"{type(e).__name__}: {e}", exc_info=True)

            return build_response(HTTPStatus.BAD_REQUEST, body)

    def add_customer() -> Dict[str, Any]:
        """
        Add customer to the DynamoDB table
        """

        # Getting the request body
        try:
            request_body = json.loads(event['body'])

            # Checking customer_id validation
            customer_id = request_body.get('customer_id')
            if msg := is_valid_id(customer_id):
                raise QueryStringsError(msg)

            customer = {
                'customer_id': customer_id
            }

            # Adding the customer ID to the DynamoDB table
            table.put_item(Item=customer)

            body = {
                'customer': customer,
                'message': 'success'
            }

            return build_response(HTTPStatus.OK, body)

        except Exception as e:
            body = {
                'message': f"{type(e).__name__}: {e}"
            }
            logger.error(f"{type(e).__name__}: {e}", exc_info=True)

            return build_response(HTTPStatus.BAD_REQUEST, body)

    def is_valid_id(customer_id: Any) -> Optional[str]:
        """
        Checking for customer_id parameter validation.
        If customer_id is valid - function returns None.
        If customer_id is not valid - function returns a message string
        that describes the error.
        """

        if not customer_id:
            return "Parameter 'customer_id' is required"

        if not isinstance(customer_id, str):
            return f"Parameter 'customer_id' requires a string"

        if ' ' in customer_id:
            return f"Parameter {customer_id=} is invalid"

    def build_response(status_code, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build and return the response object
        """

        return {
            'statusCode': status_code,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(body, indent=4)
        }

    logger.info(event)
    api_method = event['httpMethod']

    if api_method == 'GET':
        response = check_customer()
    elif api_method == 'PUT':
        response = add_customer()
    else:
        response = build_response(HTTPStatus.METHOD_NOT_ALLOWED, body={"message": "method not allowed"})

    return response
