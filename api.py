from flask import Flask
from flask_restful import Resource, Api
import twitter_tools as tt

app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def get(self, name):
        person = tt.twitter(name)
        return person

api.add_resource(Search, '/search/<name>')


if __name__ == '__main__':
    app.run(debug=True)