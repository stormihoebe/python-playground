import boto3
import pandas as pd

def my_lambda():
    output = "X"

    s3 = boto3.resource("s3")
    # data = open('iamtest.txt', 'rb')
    # s3.Bucket('py-playground').put_object(Key='test.txt', Body=data)
    # s3.Object(bucket_name='py-playground', key='test.txt')

    # 1. use boto3 to import csv file from AWS
    bucket = "py-playground"
    file_name = "pokemon_data.csv"
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=file_name)
    # - convert to data frame
    df = pd.read_csv(obj['Body'])
    # - print then csv file contents
    print(df)
    cols = df.columns
    print(cols)
    names = df['Name'][0:5]
    print(names)

    select_cols = df[['Name', 'Type 1', 'Attack', 'Defense']]
    print(select_cols)
    # iterate
    for index, row in df.iterrows():
        print(index, row['Name'], row['Type 1'])

    # filtering/locating based on params
    fire_types = df.loc[df['Type 1'] == 'Fire']
    print(len(fire_types))
    print(df.describe())

    # sorting
    sorted_df = df.sort_values(['Type 1', 'HP'], ascending=[True, False])
    print(sorted_df)

    # add column totals
    df["Total"] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
    print(df)

    # create csv
    modified_file_name = 'pokemon_modified.csv'
    new_file = df.to_csv(modified_file_name)
    data = open(modified_file_name, 'rb')

    # put new csv in s3 bucket
    s3.put_object(Bucket=bucket, Key=modified_file_name, Body=data)

    # - filter data frame down to columns

    df.loc[df['Type 1'] == 'Fire', 'Type 1'] = "Fire Type"
    df.loc[df['Generation'] == 1, 'Generation'] = "ONE"

    print(df)

    df.loc[df['Generation'] == 'ONE', 'Generation'] = 1
    print(df)

    # grouping & sorting data
    print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

    # - change values of columns (multiply)
    df["HP * Speed"] = df['HP'] * df['Speed']
    print(df)

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

    #  save as new csv file
    file_name = 'all_people.csv'
    new_file = all_people_df.to_csv(file_name)
    data = open(file_name, 'rb')

    # put new csv in s3 bucket
    s3.put_object(Bucket=bucket, Key=file_name, Body=data)

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
        row['name']
        item = build_item(row, index)
        table.put_item(
            Item=item
        )

    # 4. query dynamo db table to confirm same data

    resp = table.get_item(
        Key={'ID': 1}
    )

    print(resp['Item'])

    # create a lambda function that:
    #   reads data from s3 bucket csv file
    #   uses pandas to manipulate the data (multiply figures by 2?)
    #   adds data to dynamodb table

    # add test for lambda functions

    # create a lambda function that
    #   reads from dynamodb table by id
    # returns the output of this function

    # install the lambda on aws
    # attach a RESTful endpont to it... which i think its api gateway
    
    return output

x = my_lambda()
print(x)