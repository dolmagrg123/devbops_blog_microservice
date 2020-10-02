import boto3

client = boto3.client('dynamodb')
DB = boto3.resource('dynamodb')


__TableName__ = "BlogDB"
Primary_Column_Name = 'PostID'
Primary_Key = 1
colums = ["UserName","UserID","BlogTitle","BlogDescription"]

table = DB.Table(__TableName__)



#### How to get the data from tables
response = table.put_item (
            Item = {
                Primary_Column_Name:Primary_Key,
                colums[0]:'test',
                colums[1]:'test',
                colums[2]:'test',
                colums[3]:'test'
            }
)

# response["Item"]