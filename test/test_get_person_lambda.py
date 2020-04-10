import unittest
import get_person_lambda
import boto3
from moto import mock_dynamodb2
from unittest.mock import patch


@mock_dynamodb2
def moto_setup():
    obj = {}
    db_resource = boto3.resource('dynamodb', region_name='us-west-1')
    obj["db_resource"] = db_resource

    table = db_resource.create_table(
        TableName="People",
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )


    item_1 = {'ID': 1, 'Name': 'Ahnika', 'Age': 24}
    item_2 = {'ID': 2, 'Name': 'Storm', 'Age': 27}
    item_3 = {'ID': 3, 'Name': 'Josh', 'Age': 25}

    table.put_item(Item=item_1)
    table.put_item(Item=item_2)
    table.put_item(Item=item_3)
    obj["table"] = table

    resp = table.get_item(
        Key={'ID': 1}
    )
    obj["resp"] = resp
    return obj


class TestPersonLambda(unittest.TestCase):
    setupObj = moto_setup()

    @patch('get_person_lambda.get_table', return_value=setupObj["table"], autospec=True)
    @patch('get_person_lambda.get_item_resp', return_value=setupObj["resp"], autospec=True)
    def test_person_lambda(self, mock_get_table, mock_get_item_resp):
        actual = get_person_lambda.lambda_handler()
        expected = {'statusCode': 200, 'body': {'name': 'Ahnika', 'id': 1}}
        self.assertEqual(expected, actual)
