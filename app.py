from flask import Flask, request
from awsmanager import blog


app = Flask(__name__)
t1=blog()

### Posting 
### Comment
### Viewing 


@app.route('/posting')
def posting():
    t1.put(UserName='Sadi', UserID='123', BlogTitle="blog", BlogDescription="devbop")
    # if request.method == "POST":
    #     Content = request.form['Content']
    #     Username = request.form['Username']

    #return postingID
   

@app.route('/comment', methods=["POST"])
def comment():
    comment = request.form['Comment']
    blogID = request.form['blogID']
    #each blog content a unique ID
    status= aws.saveComment(blogID, comment)
    return  commentID


@app.route('/viewing', methods=["GET"])
def viewing():
    content = aws.getAllPost()
    return content 



if __name__ == '__main__':
    app.run(debug=True) 
