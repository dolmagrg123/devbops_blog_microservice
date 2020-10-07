from flask import Flask, request
from awsmanager import blog

blog = Blogs()
app = Flask(__name__)


### Blog 
### Comment
### Viewing 


@app.route('/createBlog', methods=['POST'])
def create():
    event.put(BlogName = "LMTD"  BlogDate = "January 1st", BlogTime = "9am", User = "Class", BlogDescription = "Enjoyed the event", BlogImage = "N/A", BlogLocation = "Slack")
    
    
    #t1.put(UserName='Sadi', UserID='123', BlogTitle="blog", BlogDescription="devbop")
    # if request.method == "POST":
    #     Content = request.form['Content']
    #     Username = request.form['Username']

    #return postingID
    #return "OK"

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
    content = aws.getAllPost()
    return content 



if __name__ == '__main__':
    app.run(debug=True) 
