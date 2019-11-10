from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
items = list()


class Title(Resource):
    def post(self):
        # REST Endpoint: http://127.0.0.1:5000/extract_vin
        # Request JSON example: {'image_url': 'https://tinyurl.com/y4umqx6t'}
        # Response JSON example: {'vin': "1VWBT7A30EC033777"}
        data = request.get_json()
        if 'image_url' not in data or data['image_url'].strip() == "":
            return {'vin': 'image url not found'}, 404
        return {'vin': "1VWBT7A30EC033777"}

class Feedback(Resource):
    def post(self):
        # REST Endpoint: http://127.0.0.1:5000/save_feedback
        # Request JSON example: {'image_url': 'https://tinyurl.com/y4umqx6t', 'feedback': 'yes'}
        # Response JSON example: {}
        data = request.get_json()
        if 'image_url' not in data or data['image_url'].strip() == "":
            return {}, 404
        print('feedback: '+data['feedback'])
        return {}

api.add_resource(Title, '/extract_vin')
api.add_resource(Feedback, '/save_feedback')

if __name__ == '__main__':
    app.run(port=5000, debug=True)