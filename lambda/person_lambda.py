import boto3
import pandas as pd
import json


def lambda_handler(event, context):
    # 1. use boto3 to import csv file from AWS
    bucket = "py-playground"
    s3 = boto3.client("s3")

    # 2. use pandas to join 2 csv files into a single data structure and print that
    people_1_file_name = 'people1.csv'
    people_2_file_name = 'people2.csv'
    obj1 = s3.get_object(Bucket=bucket, Key=people_1_file_name)
    obj2 = s3.get_object(Bucket=bucket, Key=people_2_file_name)

    df1 = pd.read_csv(obj1['Body'])
    df2 = pd.read_csv(obj2['Body'])
    # combine data to one data frame
    all_people_df = pd.concat([df1, df2])
    all_people_df.reset_index(drop=True, inplace=True)
    print(all_people_df)

    # add year column
    all_people_df['year'] = 2020 - all_people_df['age']
    print(all_people_df)

    # remove rows where name is Johny
    to_delete = all_people_df[all_people_df['name'] == 'Johny'].index
    all_people_df.drop(to_delete, inplace=True)
    print(all_people_df)

    # later:
    # 3. populate a AWS dynamo db table using pandas dataframe data, access its contents
    # known scheme

    db_resource = boto3.resource('dynamodb')
    table_name = "People"
    data_columns = all_people_df.columns
    print(data_columns)

    table_columns = ["Name", "Age"]

    table = db_resource.Table(table_name)
    data_columns = all_people_df.columns
    print(data_columns)

    def build_item(row_data, ind):
        person = {
            "ID": ind,
            "Name": row_data["name"],
            "Age": row_data["age"]
        }
        return person

    # iterate
    for index, row in all_people_df.iterrows():
        item = build_item(row, index)
        table.put_item(
            Item=item
        )

    # 4. query dynamo db table to confirm same data

    resp = table.get_item(
        Key={'ID': 1}
    )

    item = {'name': resp['Item']['Name']}

    # install the lambda on aws
    # attach a RESTful endpont to it... which i think its api gateway

    output = {'statusCode': 200, 'body': item}

    return output
