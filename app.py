from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.video import VideoResource
import os

app = Flask(__name__)

CORS(app)
api = Api(app)


api.add_resource(VideoResource, '/video/')


@app.route('/', methods=['GET'])
def welcome():
    return "Credit:"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
