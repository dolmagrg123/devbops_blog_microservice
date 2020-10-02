from flask import Flask, request
import awsmanager.py


app = Flask(__name__)

### Posting 
### Comment
### Viewing 


@app.route('/posting', methods=["POST"])
def posting():
    if request.method == "POST":
        Content = request.form['Content']
        Username = request.form['Username']
        
    return postingID
   

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
