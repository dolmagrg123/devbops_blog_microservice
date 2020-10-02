import boto3



class blog:
    def __init__(self):
        self.__Tablename__ = "BlogDB"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "PostID"
        self.Primary_key = 1
        self.columns = ["UserName","UserID","BlogTitle","BlogDescription"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, UserName, UserID, BlogTitle, BlogDescription):
        all_items = self.table.scan()
        last_primary_key = len(all_items['Items']) + 1

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:last_primary_key,
                self.columns[0]: userName,
                self.columns[1] : UserID,
                self.columns[2] : BlogTitle,
                self.columns[3] : BlogDescription
                
                


            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])
t1=blog()
t1.put(userName='Sadi', UserID='123', BlogTitle="blog", BlogDescription="devbop")