#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from core.model import ModelWrapper
from maxfw.core import MAX_API, PredictAPI
from flask_restplus import fields
from flask import abort

# Set up parser for input data (http://flask-restplus.readthedocs.io/en/stable/parsing.html)
input_parser = MAX_API.parser()
input_parser.add_argument('first_word', type=str, required=True,
                          help="utf-8 encoded Chinese word.")
input_parser.add_argument('second_word', type=str,
                          help="utf-8 encoded Chinese word.")
input_parser.add_argument('mode', type=str, default='simplified', choices=['simplified', 'traditional'],
                          help="Chinese: simplified or traditional.")
input_parser.add_argument('theta', type=int, default=1,
                          help="Distance threshold for number of candidate words to return. A higher theta returns more"
                               "candidate words")


# Creating a JSON response model: https://flask-restplus.readthedocs.io/en/stable/marshalling.html#the-api-model-factory

label_prediction = MAX_API.model('Prediction', {
    'distance': fields.String(required=True, description='Label identifier'),
    'candidates': fields.List(fields.List(fields.String), description='Nearest candidates')
})

predict_response = MAX_API.model('ModelPredictResponse', {
    'status': fields.String(required=True, description='Response status message'),
    'predictions': fields.List(fields.Nested(label_prediction), description='Predicted labels and probabilities')
})


class ModelPredictAPI(PredictAPI):

    model_wrapper = ModelWrapper()

    @MAX_API.doc('predict')
    @MAX_API.expect(input_parser)
    @MAX_API.marshal_with(predict_response)
    def post(self):
        """Make a prediction given input data"""
        result = {'status': 'error'}
        args = input_parser.parse_args()

        text = [args['first_word']]
        if args['first_word'] == "":
            abort(400, "Please provide a valid input string.")

        if args['second_word']:
            text.append(args['second_word'])
        theta = args['theta']
        mode = args['mode']
        input_json = {'text': text, 'theta': theta, 'mode': mode}

        try:
            preds = self.model_wrapper.predict(input_json)
        except:  # noqa
            abort(400, "Invalid input to Pinyin converter, please check!")

        result['predictions'] = preds
        result['status'] = 'ok'

        return result
