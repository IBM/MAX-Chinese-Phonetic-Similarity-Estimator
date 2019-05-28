# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Chinese Phonetic Similarity Estimator'
API_DESC = 'Calculate phonetic similarity and get close candidate words to a given Chinese word.'
API_VERSION = '1.1.0'

# default model
MODEL_NAME = 'dimsim'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
MODEL_LICENSE = 'ApacheV2'

MODEL_META_DATA = {
    'id': '{}'.format(MODEL_NAME.lower()),
    'name': '{} Python Model'.format(MODEL_NAME),
    'description': '{} - A Chinese soundex library '.format(MODEL_NAME),
    'type': 'Text/Soundex models',
    'source': 'https://developer.ibm.com/exchanges/models/all/max-chinese-phonetic-similarity-estimator/',
    'license': '{}'.format(MODEL_LICENSE)
}