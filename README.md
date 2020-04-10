# Playing around with Python, Pandas, Lambdas, s3, Dynamodb

## Learning Materials 
### python: https://www.youtube.com/watch?v=_uQrJ0TkZlc
### pandas: https://www.youtube.com/watch?v=vmEHCJofslg
### boto3 overview: https://www.youtube.com/watch?v=JiASzk_bH5M
### dynamodb: https://www.youtube.com/watch?v=Al1xwYhQ-BM
### lambda & dynamodb https://www.youtube.com/watch?v=8zhv6GDSDE8
### lambda functions & aws cli https://www.youtube.com/watch?v=Vdjt59dh0gs
### lambda w/ dynamodb & s3 bucket in python https://www.youtube.com/watch?v=-8L4OxotXlE
### how to use pandas in aws lambda https://www.youtube.com/watch?v=vf1m1ogKYrg
- gotcha with using pandas in lambda - include numpy, pandas, pytz 
- download files from from https://pypi.org/
- choose these versions: `{module-name}-version-cp37-cp37m-manylinux1_x86_64.whl` because they are the only ones that will run in the lambda when deployed to aws
### api gateway w/ lambda https://www.youtube.com/watch?v=uFsaiEhr1zs
- Gotcha with setting up api gateway: https://stackoverflow.com/questions/47624509/aws-error-proxy-integrations-cannot-be-configured-to-transform-responses

### testing in python https://www.youtube.com/watch?v=6tNS--WetLI
### testing lambdas with moto https://www.youtube.com/watch?v=11Fr0wqcxRc&t=381s

## Files 
`./test.py` is working with python basics

`./app.py` is using boto3, pandas, & dynamodb

`./lambda/person_lambda.py` is a lambda function that takes 2 csv files from s3, combines them, manipulates the data, adds the data to a dynamodb table. Then requests an item from the table and returns the name of the first person

`./lambda/zip.zip` is what actually got uploaded to aws lambda, it includes the python file as well as the dependencies (for the specific version/runtime aws uses) 

the lambda function is triggered by this api gateway, which is currently returning an error 🙂 https://1901omd98b.execute-api.us-west-2.amazonaws.com/default/personFunction