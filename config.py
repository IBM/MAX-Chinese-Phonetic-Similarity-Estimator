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
# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Chinese Phonetic Similarity Estimator'
API_DESC = 'Estimate the phonetic distance between Chinese words and get similar sounding candidate words.'
API_VERSION = '1.2.0'

# default model
MODEL_NAME = 'dimsim'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
MODEL_LICENSE = 'Apache V2'

MODEL_META_DATA = {
    'id': '{}'.format(MODEL_NAME.lower()),
    'name': '{} Python Model'.format(MODEL_NAME),
    'description': '{} - A Chinese soundex library '.format(MODEL_NAME),
    'type': 'Text/Soundex models',
    'source': 'https://developer.ibm.com/exchanges/models/all/max-chinese-phonetic-similarity-estimator/',
    'license': '{}'.format(MODEL_LICENSE)
}
