from flask import Flask, request
from awsmanager import Blog

blog = Blog()
app = Flask(__name__)





### Blog 
### Comment
### Viewing 

{
    "BlogName": {blogname}, 
    "BlogDate": {date}, 
    "BlogTime": {time}, 
    "UserID": {userid}, 
    "BlogContent": {content}, 
    "BlogImage": {img},  # img will be a base64 encoding string
    "BlogLocation": {location}, 
    "BlogComment": {{dict}}
}

@app.route('/createBlog', methods=['POST'])
def create():
    res = request.json
    blogname = res['BlogName']
    blogdate = res['BlogData']
    blogtime = res['BlogTime']
    userid = res['UserID']
    blogcontent = res['BlogContent']
    blogimage = res['BlogImage']
    bloglocation = res['BlogLocation']
    blogcomment = res['BlogComment']

    res = blog.put(BlogName=blogname, BlogDate=blogdate, BlogTime=blogtime, UserID=userid, BlogContent=blogcontent, BlogImage=blogimage, BlogLocation=bloglocation, BlogComment=blogcomment)

    print(res) ## only here for debugging
    return res

@app.route('/update', methods=['POST'])
def updateBlog():
    res = request.json
    blogID= res['blogID']
    blogname = res['New_BlogName']
    blogdate = res['New_BlogData']
    blogtime = res['New_BlogTime']
    blogcontent = res['New_BlogContent']
    blogimage = res['New_BlogImage']
    bloglocation = res['New_BlogLocation']
    blogcomment = res['New_BlogComment']

    res = blog.put(blogID=blogID, BlogName=New_blogname, BlogDate=blogdate, BlogTime=blogtime, UserID=userid, BlogContent=blogcontent, BlogImage=blogimage, BlogLocation=bloglocation, BlogComment=blogcomment)
    return res



@app.route('/delete', methods=['POST'])
def deleteBlog():
    req = request.json
    blogID = req['BlogID']
    res = blog.delete(blogID)
    return res

### NEED TO WORK ON COMMENT ###
@app.route('/comment', methods=["POST"])
def comment():
    comment = request.form['Comment']
    blogID = request.form['blogID']
    ## generate a commentID by using UUID
    #commentID = UUID()
    #each blog content a unique ID
    status= aws.saveComment(commentID, blogID, comment)
    #return  commentIDclear
    return "OK"


@app.route('/viewing', methods=["GET"])
def viewing():
    res = blog.view()
    return res



if __name__ == '__main__':
    app.run(debug=True) 
