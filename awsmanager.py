import boto3
from boto3.dynamodb.conditions import Attr 


#Using DevBops_blog
#Columns are : "BlogName", "BlogDate", "BlogTime", "UserID", "BlogContent", "BlogImage", "BlogLocation", "BlogComment"
# BloagCommnet should be a dictionary, key is the userid, value is their comments

# Response template:
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
        self.Primary_Column_Name = "blogID"
        self.Primary_key = 1
        self.columns = ["BlogName", "BlogDate", "BlogTime", "UserID", "BlogContent", "BlogImage", "BlogLocation", "BlogComment"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, BlogName, BlogDate, BlogTime, UserID, BlogContent, BlogImage, BlogLocation, BlogComment):
        
        # cehck if blog exists, if exists, then immediately return false
        if(self.check_blog_exists(BlogName)):
            # immediately return false
            return {
                "Result": False,
                "Error": "Blog was created",
                "Description": "Blog name already exists",
                "BlogID": None
            }

        
        all_items = self.table.scan()
        last_primary_key = len(all_items['Items']) +1

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:last_primary_key,
                self.columns[0]: BlogName,
                self.columns[1] : BlogDate,
                self.columns[2] : BlogTime,
                self.columns[3] : UserID,
                self.columns[4] : BlogContent,
                self.columns[5] : BlogImage,
                self.columns[6] : BlogLocation,
                self.columns[7] : BlogComment
            }
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "Description": "Blog was created succesfully",
                "BlogID": last_primary_key
        
            }
        else:
           return {
               "Result": False,
                "Error": "Database error",
                "Description": "Database error",
                "BlogID": None
           } 

    def check_blog_exists(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("BlogName").eq(BlogName)
        )
        if response["Items"]:
            # We found blog already exists
            return True
        else:
            return False

    def update_blog(self, BlogID, New_BlogName, New_BlogDate, New_BlogTime, New_BlogContent,  New_BlogImage, New_BlogLocation ):
        
        response = self.table.scan(
            FilterExpression=Attr("blogID").eq(BlogID)
        )

        if response["Items"]:
    #         # TODO: use update_item insetad of put_item
            #self.Primary_key = response["Items"][0]["blogID"]
            self.Primary_key = response["Items"][0]["blogID"]
            res = self.table.update_item(
                Key={
                    'blogID' :blogID,
                    'BlogName':New_BlogName,
                    'BlogDate':New_BlogDate,
                    'BlogTime':New_BlogTime,
                    'BlogContent':New_BlogContent,
                    'BlogImage':New_BlogImage,
                    'BlogLocation':New_BlogLocation
                        
                },
                UpdateEpression ="set BlogContent=:c",
                ExpressionAttributeValues={
                    ':c':New_BlogContent
                    
                 },
                
                    # Item = {
                    #     self.Primary_Column_Name:self.Primary_key,
                    #     self.columns[0]: New_BlogName,
                    #     self.columns[1] : New_BlogDate,
                    #     self.columns[2] : New_BlogTime,
                    #     self.columns[3] : New_BlogContent,
                    #     self.columns[4] : New_BlogImage,
                    #     self.columns[5] : New_BlogLocation
                    #   }
                 
            )

            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "Blog was updated succesfully",
                
                    "BlogID": None

                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error",
                    "BlogID": None
                } 
        else:
            return {

                "Result": False,
                "Error": "Blog not found",
                "Description": "Cannot updated",
                "BlogID": None

            }
        


    def delete(self, BlogID):
        response = self.table.scan(
            FilterExpression=Attr("blogID").eq(BlogID)
        )
        if response["Items"]:
             self.Primary_key = response["Items"][0]["blogID"]
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
    #res = blog.put(BlogName="test1234", BlogDate="OCT 4,2020", BlogTime="3 pm", UserID="Sadika C", BlogContent="coding", BlogImage="img", BlogLocation="NY", BlogComment={})
    
    #for update post
    #res = blog.update_blog(BlogID=1, New_BlogName="LMTD", New_BlogDate='Nov 6, 2020', New_BlogTime='3 PM', New_BlogContent='testing update',  New_BlogImage="img", New_BlogLocation="NY")
    
    # for delete
    #res = blog.delete(3)
    
    # for view
    #res = blog.view()

    print(res)