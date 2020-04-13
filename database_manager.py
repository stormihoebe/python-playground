import boto3
import pandas as pd
import psycopg2

file_name = "people.csv"
file_source_local = True

db_host = "localhost"
db_name = "pyplayground"

table_name = "People"
bucket = "py-playground"
s3 = boto3.client("s3")


def fetch_csv_data(filename):
    if file_source_local:
        people_df = pd.read_csv(file_name)
    else:
        obj = s3.get_object(Bucket=bucket, Key=filename)
        people_df = pd.read_csv(obj['Body'])
    return people_df


def get_dynamodb_table(t_name):
    db_resource = boto3.resource('dynamodb')
    table = db_resource.Table(t_name)
    return table


def get_dynamodb_item_by_id(table, guid):
    r = table.get_item(
        Key={'ID': guid}
    )
    item = r.get("Item", None)
    return item


def build_dynamodb_item(row_data, ind):
    person = {
        "ID": ind,
        "Name": row_data["name"],
        "Age": row_data["age"]
    }
    return person


def update_databases_with_csv():
    csv_data = fetch_csv_data(file_name)
    table = get_dynamodb_table(table_name)

    con = create_sql_db_connection(db_host, db_name)

    for index, row in csv_data.iterrows():
        # check & create for dynamodb
        existing_item = get_dynamodb_item_by_id(table, index)
        if existing_item is None:
            item = build_dynamodb_item(row, index)
            table.put_item(
                Item=item
            )
            print(f"added new item {index} to dynamo db")
        else:
            print(f"item {index} already exists in dynamo db")
        # check & create for sql db
        existing_sql_item = get_sql_item_by_id(con, index)
        if existing_sql_item is None:
            add_item_to_sql_db(con, row, index)
            print(f"added new item {index} to dynamo sql db")
        else:
            print(f"item {index} already exists in sql db")

    all_dynamo_items = table.scan()["Items"]
    all_sql_items = get_all_sql_items(con)
    return {
        "dynamo_people": all_dynamo_items, "psql_people": all_sql_items
    }


def create_sql_db_connection(host, name):
    connection = psycopg2.connect(
        host=db_host,
        database=db_name
    )
    return connection


def get_sql_item_by_id(con, guid):
    cur = con.cursor()
    cur.execute(f"select name, age, id from person where id = '{guid}'")
    items = cur.fetchall()

    cur.close()
    if len(items) == 0:
        return None
    else:
        return items[0]


def get_all_sql_items(con):
    cur = con.cursor()
    cur.execute("select name, age, id from person")
    items = cur.fetchall()

    cur.close()
    return items


def add_item_to_sql_db(con, item, ind):
    cur = con.cursor()
    name = item['name']
    age = item['age']
    cur.execute(f"insert into person (id, name, age) values({ind}, '{name}', {age})")
    con.commit()
    cur.close()
