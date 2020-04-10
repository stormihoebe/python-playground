import boto3


def lambda_handler(id=1):
    table = get_table("People")
    resp = get_item_resp(table, id)

    item = {'name': resp['Item']['Name'], 'id': id}

    output = {'statusCode': 200, 'body': item}
    print(output)

    return output


def get_table(table_name):
    db_resource = boto3.resource('dynamodb')
    return db_resource.Table(table_name)


def get_item_resp(table, id):
    resp = table.get_item(
        Key={'ID': id}
    )
    return resp
