from flask import Flask, request
from awsmanager import Blog
blog = Blog()
app = Flask(__name__)
### Blog 
### Comment
### Viewing 
# {
#     "BlogName": {blogname}, 
#     "BlogDate": {date}, 
#     "BlogTime": {time}, 
#     "UserID": {userid}, 
#     "BlogContent": {content}, 
#     "BlogImage": {img},  # img will be a base64 encoding string
#     "BlogLocation": {location}, 
#     "BlogComment": {{dict}}
# }
@app.route('/createBlog', methods=['POST'])
def create():
    res = request.json
    blogname = res['BlogName']
    blogdate = res['BlogDate']
    blogtime = res['BlogTime']
    userid = res['UserID']
    blogcontent = res['BlogContent']
    blogimage = res['BlogImage']
    bloglocation = res['BlogLocation']
    blogcomment = res['BlogComment']
    res = blog.put(BlogName=blogname, BlogDate=blogdate, BlogTime=blogtime, UserID=userid, BlogContent=blogcontent, BlogImage=blogimage, BlogLocation=bloglocation, BlogComment=blogcomment)
    #print(res) ## only here for debugging
    return res
@app.route('/update', methods=['POST'])
def updateBlog():
    res = request.json
    blogname = res['blogName']
    blogdate = res['New_BlogDate']
    blogtime = res['New_BlogTime']
    blogcontent = res['New_BlogContent']
    blogimage = res['New_BlogImage']
    bloglocation = res['New_BlogLocation']
    res = blog.update_blog(BlogName=blogname, BlogDate=blogdate, BlogTime=blogtime, BlogContent=blogcontent, BlogImage=blogimage, BlogLocation=bloglocation)
    return res
@app.route('/delete', methods=['POST'])
def deleteBlog():
    req = request.json
    BlogName = req['BlogName']
    res = blog.delete(BlogName)
    return res
### NEED TO WORK ON COMMENT ###
@app.route('/comment', methods=["POST"])
def comment():
    req = request.json
    BlogName = req['BlogName']
    res = blog.add_comment # Does this work?
    return res
    ## generate a commentID by using UUID
    #commentID = UUID()
    #each blog content a unique ID
    #return  commentIDclear
   # return "OK"
@app.route('/viewing', methods=["GET"])
def viewing():
    res = blog.view()
    return res
if __name__ == '__main__':
    app.run(debug=True)