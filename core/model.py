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

        output_json['candidates'] = [dimsim.get_candidates(i, mode, theta) for i in input_strings]

        return output_json
