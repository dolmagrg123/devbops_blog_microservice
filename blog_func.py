import boto3

class BlogManager:
    def __init__(self):
        self.BLOG = {}
        self.load()
