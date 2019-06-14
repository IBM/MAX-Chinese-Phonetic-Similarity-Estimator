from maxfw.model import MAXModelWrapper

import logging
from config import DEFAULT_MODEL_PATH
import dimsim
from config import MODEL_META_DATA as model_meta

logger = logging.getLogger()


class ModelWrapper(MAXModelWrapper):

    MODEL_META_DATA = model_meta

    def __init__(self, path=DEFAULT_MODEL_PATH):
        logger.info('Loading model from: {}...'.format(path))

        # Load the graph

        # Set up instance variables and required inputs for inference
        logger.info('Loaded model')

    def _pre_process(self, input):
        return input

    def _post_process(self, result):
        return result

    def _predict(self, x):
        mode = x.get('mode', 'simplified')
        theta = x.get('theta', 1)
        input_strings = x['text']

        output_json = {}

        if len(input_strings) == 2:
            output_json['distance'] = dimsim.get_distance(input_strings[0], input_strings[1])
        else:
            output_json['distance'] = 0

        output_json['candidates'] = {}
        output_json['candidates']['first_word'] = dimsim.get_candidates(input_strings[0], mode, theta)

        if len(input_strings) == 2:
            output_json['candidates']['second_word'] = dimsim.get_candidates(input_strings[0], mode, theta)
        else:
            output_json['candidates']['second_word'] = []

        return output_json
