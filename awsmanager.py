import boto3
from boto3.dynamodb.conditions import Attr 

class blog:
    def __init__(self):
        self.__Tablename__ = "BlogDB"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "BlogID"
        self.Primary_key = 1
        self.columns = ["BlogName", "BlogDate", "BlogTime", "User", "BlogDescription", "BlogImage", "BlogLocation"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, BlogName, BlogDate, BlogTime, User, BlogDescription, BlogImage, BlogLocation):
        all_items = self.table.scan()
        last_primary_key = len(all_items['Items']) + 1

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:last_primary_key,
                self.columns[0]: self.check_if_blog_exists(Event_name),
                self.columns[1] : BlogDate,
                self.columns[2] : BlogTime,
                self.columns[3] : User,
                self.columns[4] : BlogDescription,
                self.columns[5] : BlogImage,
                self.columns[6] : BlogLocation
            }
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "description": "Blog was created succesfully",
                "Primary_key": last_primary_key,
                 "BlogName": BlogName,
                 "BlogDate":  BlogDate,
                 "BlogTime":  BlogTime,
                 "User": User,
                 "BlogDescription": BlogDescription,
                 "BlogImage":  BlogImage,
                 "BlogLocation": BlogLocation

            }
        else:
            return {
                "Results": False,
                "Error": "Blog was not created"
            }

    def check_if_blog_exists(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("BlogName").eq(BlogName)
        )
        if response["Items"]:
            return {
                "Result": False,
                "Error": "Blog already exists"
            }
        else:
            return BlogName

    def update_blog(self, BlogName, New_BlogName, New_BlogDate, New_BlogTime, NewUser,  New_BlogDescription,  New_BlogImage, New_BlogLocation ):
        response = self.table.scan(
            FilterExpression=Attr("BlogName").eq(BlogName)
        )

    if response["Items"]:
            self.Primary_key = response["Items"][0]["BlogId"]
            res = self.table.put_item(
                    Item = {
                        self.Primary_Column_Name:self.Primary_key,
                        self.columns[0]: New_BlogName,
                        self.columns[1] : New_BlogDate,
                        self.columns[2] : New_BlogTime,
                        self.columns[3] : New_User,
                        self.columns[4] : New_BlogDescription,
                        self.columns[5] : New_BlogImage,
                        self.columns[6] : New_BlogLocation

                     }
                 
            )

            return {

                 "Primary_key": self.Primary_key,
                 "New_BlogName": New_BlogName,
                 " New_BlogDate": New_BlogDate,
                 " New_BlogTime": New_BlogTime,
                 "New_User": New_User,
                 " New_BlogDescription": New_BlogDescription,
                 " New_BlogImage":  New_BlogImage,
                 "New_BlogLocation": New_BlogLocation


            }
    else:
        return {
            "Results": False,
            "Error": "Blog doesnt exists"
                
        }


    def delete(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("BlogName").eq(BlogName)
        )
        if response["Items"]:
             self.Primary_key = response["Items"][0]["BlogId"]
             res = self.table.delete_item(
                 Key={
                     self.Primary_Column_Name:self.Primary_key

                 }
             )
             return {
                 "Result": True,
                 "Error": None,
                 "description": "Blog was deleted"
             }
        else:
            return {
                "Result": False,
                "Error": "Blog does not exists"
            }
    
#print(response["ResponseMetadata"]["HTTPStatusCode"])
# t1=blog()
# t1.put(UserName='Sadi', UserID='123', BlogTitle="blog", BlogDescription="devbop")



