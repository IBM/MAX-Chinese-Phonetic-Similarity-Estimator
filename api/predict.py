from core.model import ModelWrapper
from maxfw.core import MAX_API, PredictAPI
from flask_restplus import fields
from flask_restplus import abort

# Set up parser for input data (http://flask-restplus.readthedocs.io/en/stable/parsing.html)
input_parser = MAX_API.parser()
input_parser.add_argument('first_word', type=str, required=True,
                          help="utf-8 encoded Chinese word.")
input_parser.add_argument('second_word', type=str,
                          help="utf-8 encoded Chinese word.")
input_parser.add_argument('mode', type=str, default='simplified', choices=['simplified', 'traditional'],
                          help="Chinese: simplified or traditional.")
input_parser.add_argument('theta', type=int, default=1,
                          help="Distance threshold for number of candidate words to return. A higher theta returns more "
                               "candidate words.")


# Creating a JSON response model: https://flask-restplus.readthedocs.io/en/stable/marshalling.html#the-api-model-factory

candidates_response = MAX_API.model('CandidatesResponse', {
                    'first_word': fields.List(fields.String, description='Nearest candidates to first_word'),
                    'second_word': fields.List(fields.String, description='Nearest candidates to second_word')
                })

label_prediction = MAX_API.model('Prediction', {
    'distance': fields.Float(required=True, description='Label identifier'),
    'candidates': fields.Nested(candidates_response, required=True, description='candidates')
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
        if args['second_word']:
            text.append(args['second_word'])
        theta = args['theta']
        mode = args['mode']
        input_json = {'text': text, 'theta': theta, 'mode': mode}

        try:
            preds = self.model_wrapper.predict(input_json)
        except TypeError or UnicodeDecodeError:  # noqa
            abort(400, errors='first_word, second_word', message="The input format is not valid. "
                  "Please input utf-8 encoded Chinese word(s) only.")

        result['predictions'] = preds
        result['status'] = 'ok'

        return result
