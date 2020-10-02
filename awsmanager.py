import boto3

client = boto3.client('dynamodb', aws_access_key_id='devlmtd2', aws_secret_access_key='UEHYKCRvAdX7OvRPuuAhTll4VwqDEvDQC7HiOyCV', region_name = 'us-east-1')
client = boto3.client('dynamodb', region_name='us-east-1')


__TableName__ = "BlogDB1"
Primary_Column_Name = 'PostID'
Primary_Key = 0
colums = ["UserName","UserID","BlogTitle","BlogDescription"]

client = boto3.client ('dynamodb')
DB = boto3.resource('dynamodb')

table = DB.Table(__TableName__)



#### How to get the data from tables
# respone = table.get_item (
#             Key = {
#                 Primary_Column_Name:Primary_Key
#             }
# )

# response["Item"]