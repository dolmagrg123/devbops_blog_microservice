"# devbops_blog_microservice" 

# Primary Key = BlogName

## Create Blog
        for /createBlog ,
 {
    "BlogName": {blogname}, 
     "BlogDate": {date}, 
    "BlogTime": {time}, 
     "UserName": {username}, 
     "BlogContent": {content}, 
     "BlogImage": {img},  # img will be a base64 encoding string
    "BlogLocation": {location}, 
     "BlogComment": {{dict}}
 }

Request method type: POST

 # Response will be

 {
    "BlogName": "dictionary",
    "Description": "Blog was created succesfully",
    "Error": null,
    "Result": true
}


## Update Blog
    Request method type: POST

 FOR /update,
 {
   " "BlogName": {blogname}, 
     "BlogDate": {date}, 
     "BlogTime": {time}, 
     "UserName": {username}, 
     "BlogContent": {content}, 
     "BlogImage": {img},  # img will be a base64 encoding string
     "BlogLocation": {location}, 
    "

# Response will be 

{
    "BlogName": null,
    "Description": "Cannot updated",
    "Error": "Blog not found",
    "Result": false
}

## Delete Blog
    Request method type: GET

FOR /delete

{

        "BlogName":{blogname}

}

# Response will be 

{
    "Error": null,
    "Result": true,
    "description": "Blog was deleted"
}

## Add Comment
    Request method type: POST

FOR /comment

{
 
 "BlogName": {blogname},
 "UserName": {username},
 "Comment" : {comment}

}

# Response will be

{
    "BlogName": null,
    "Description": "Comment was updated succesfully",
    "Error": null,
    "Result": true
}

## View Blog
    Request method type: GET

FOR /view

res = blog.view()
return res

# This is to view our blog
   

