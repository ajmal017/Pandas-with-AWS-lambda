import pandas as pd
import boto3
from io import StringIO

def lambda_handler(event, context):
	s3_file_key = 'exec_3.csv'
	bucket = 'execbk2'

	s3 = boto3.client('s3')
	obj = s3.get_object(Bucket=bucket, Key=s3_file_key)
	body=obj['Body']
	mycsv_string = body.read().decode('utf-8')
	df = pd.read_csv(StringIO(mycsv_string))
	print(df.head(5))
	print(df.dtypes)
	print(df.groupby(['pname', 'timelvl'])['val'].agg('sum'))