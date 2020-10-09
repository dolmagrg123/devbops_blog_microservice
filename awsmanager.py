import boto3
from boto3.dynamodb.conditions import Attr 
#Using DevBops_blog
#Columns are : "BlogName", "BlogDate", "BlogTime", "UserID", "BlogContent", "BlogImage", "BlogLocation", "BlogComment"
# BlogCommnet should be a dictionary, key is the userid, value is their comments
# Response template:
#Using DevBops_blog
#Columns are : "BlogName", "BlogDate", "BlogTime", "UserID", "BlogContent", "BlogImage", "BlogLocation", "BlogComment"
# BlogCommnet should be a dictionary, key is the userid, value is their comments
###Response template:
#return {
#                "Result": False or True,
#                "Error": None or errorMessage,
#                "Description": "",
#                "BlogID": None or blogID
#            }
class Blog:
    def __init__(self):
        self.__Tablename__ = "DevBops_blog"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "blogName"
        self.Primary_key = "blogName"
        self.columns = ["BlogDate", "BlogTime", "UserID", "BlogContent", "BlogImage", "BlogLocation", "BlogComment"]
        self.table = self.DB.Table(self.__Tablename__)
    def put(self, BlogName, BlogDate, BlogTime, UserID, BlogContent, BlogImage, BlogLocation, BlogComment):
        
        # cehck if blog exists, if exists, then immediately return false
        if(self.check_blog_exists(BlogName)):
            # immediately return false
            return {
                "Result": False,
                "Error": "Blog cannot be created",
                "Description": "Blog name already exists",
                "BlogName": None
            }
        
        # all_items = self.table.scan()
        # last_primary_key = len(all_items['Items']) +1
      

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:BlogName,
                # self.columns[0]: BlogName,
                self.columns[0] : BlogDate,
                self.columns[1] : BlogTime,
                self.columns[2] : UserID,
                self.columns[3] : BlogContent,
                self.columns[4] : BlogImage,
                self.columns[5] : BlogLocation,
                self.columns[6] : BlogComment
            }
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "Description": "Blog was created succesfully",
                "BlogName": BlogName
        
            }
        else:
           return {
               "Result": False,
                "Error": "Database error",
                "Description": "Database error",
                "BlogName": None
           } 
    def check_blog_exists(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:
            # We found blog already exists
            return True
        else:
            return False
    def update_blog(self, BlogName, New_BlogDate, New_BlogTime, New_BlogContent,  New_BlogImage, New_BlogLocation ):
        
        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:
             # ###### TODO: use update_item insetad of put_item
            #self.Primary_key = response["Items"][0]["blogID"]
            # self.Primary_key = response["Items"][0]["blogName"]
            res = self.table.update_item(
                Key={
                    'blogName' :BlogName,   
                        
                },
               UpdateExpression="set BlogDate=:d, BlogTime=:t, BlogImage=:i, BlogLocation=:l, BlogContent=:c",
               ExpressionAttributeValues={
                    # ':n': New_BlogName,
                    ':d': New_BlogDate,
                    ':t': New_BlogTime,
                    ':i': New_BlogImage,
                    ':l': New_BlogLocation,
                    ':c': New_BlogContent
                },
                ReturnValues="UPDATED_NEW"
                 
            )
            return res
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "Blog was updated succesfully",
                
                    "BlogName": None
                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error",
                    "BlogName": None
                } 
        else:
            return {
                "Result": False,
                "Error": "Blog not found",
                "Description": "Cannot updated",
                "BlogName": None
            }
    def delete(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:
             self.Primary_key = response["Items"][0]["blogName"]
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
    
    def view(self):
        res = self.table.scan()
        return res['Items']
if __name__ == "__main__":
    blog = Blog()
    #for create new post
    res = blog.put(BlogName="One", BlogDate="OCT 8,2020", BlogTime="10 AM", UserID="Sadika C", BlogContent="NewPrimary", BlogImage="img", BlogLocation="NY", BlogComment="None")
    res = blog.put(BlogName="Three", BlogDate="OCT 9,2020", BlogTime="10 AM", UserID="Chandler", BlogContent="Making new", BlogImage="img", BlogLocation="NY", BlogComment="None")
    #for update post
    #res = blog.update_blog(BlogName="One", New_BlogDate='OCT 09, 2020', New_BlogTime='5 PM', New_BlogContent='update workingV1',  New_BlogImage="img", New_BlogLocation="NY")
    
    # for delete
    #res = blog.delete("One")
    
    # for view
    res = blog.view()
print (res)