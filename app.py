from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
items = list()


class DemoOCR(Resource):
    def post(self):
        # POST Request example: http://127.0.0.1:5000/extract_vin
        # request JSON example: {'image_url': 'https://tinyurl.com/y4umqx6t'}
        data = request.get_json()
        if 'image_url' not in data or data['image_url'].strip() == "":
            return {'vin': None}, 404
        return {'vin': "1VWBT7A30EC033777"}

api.add_resource(DemoOCR, '/extract_vin')

if __name__ == '__main__':
    app.run(port=5000, debug=True)