## Revolut Python Engineer Data Challenge
##
## Author: Sérgio Mafra <sergio@mafra.io>
## Coded Date: 2019-03-24
## Editor: Vim
##

from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from flask_httpauth import HTTPBasicAuth
from classes.Nest import Nest
import json


app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

## Credentials to access the API
USER_CREDS = {
    'revolut': 'YouWillNeverFindOut'
}

## Method to verify if the specified user can access the API
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_CREDS.get(username) == password

class NestAPI(Resource):
    @auth.login_required
    def get(self):

        ## Parsing arguments
        parser = reqparse.RequestParser()
        parser.add_argument('file')
        parser.add_argument('level', action='append')
        args = parser.parse_args()

        ## Instantiating Nest()
        nest = Nest()

        ## Preparing data
        json_data = nest.read_input_from_file(args['file'])
        output_dict = nest._prepare_output(json_data, args['level'])

        ## Making sure the browser will interpret
        ## the json format correctly
        response = make_response(json.dumps(output_dict, indent=2,
            sort_keys=True))
        response.headers['content-type'] = 'application/json'

        return response

api.add_resource(NestAPI, '/nest', endpoint='nest')

if __name__ == '__main__':
    app.run(debug=True)
