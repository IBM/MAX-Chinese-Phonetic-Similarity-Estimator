# -*- coding: utf-8 -*-
import pytest
import requests


def test_swagger():

    model_endpoint = 'http://localhost:5000/swagger.json'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200
    assert r.headers['Content-Type'] == 'application/json'

    json = r.json()
    assert 'swagger' in json
    assert json.get('info') and json.get('info').get('title') == 'MAX Chinese Phonetic Similarity Estimator'


def test_metadata():

    model_endpoint = 'http://localhost:5000/model/metadata'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200

    metadata = r.json()
    assert metadata['id'] == 'dimsim'
    assert metadata['name'] == 'dimsim Python Model'
    assert metadata['description'] == 'dimsim - A Chinese soundex library '
    assert metadata['license'] == 'ApacheV2'


def test_response():
    model_endpoint = 'http://localhost:5000/model/predict'
    params = {
        "first_word": u"大侠",
        "second_word": "",
        "mode": 'simplified',
        "theta": 1
    }
    r = requests.post(url=model_endpoint, params=params)

    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['distance'] == str(0)


def test_response_close():
    model_endpoint = 'http://localhost:5000/model/predict'
    params = {
        "first_word": u"大侠",
        "second_word": u"大虾",
        "mode": 'simplified',
        "theta": 1
    }
    r = requests.post(url=model_endpoint, params=params)

    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['distance'] == str(0.0002380952380952381)


def test_response_far():
    model_endpoint = 'http://localhost:5000/model/predict'
    params = {
        "first_word": u"大侠",
        "second_word": u"大人",
        "mode": 'simplified',
        "theta": 1
    }
    r = requests.post(url=model_endpoint, params=params)

    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['distance'] == str(25.001417183349876)


def test_response_candidates():
    model_endpoint = 'http://localhost:5000/model/predict'
    params = {
        "first_word": u"大侠",
        "second_word": "",
        "mode": 'simplified',
        "theta": 1
    }
    r = requests.post(url=model_endpoint, params=params)

    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['distance'] == str(0)
    assert response['predictions'][0]['candidates'][0] is not None


def test_invalid_input():
    model_endpoint = 'http://localhost:5000/model/predict'
    params = {
        "first_word": "abcde",
        "second_word": "",
        "mode": 'simplified',
        "theta": 1
    }
    r = requests.post(url=model_endpoint, params=params)

    assert r.status_code == 400


if __name__ == '__main__':
    pytest.main([__file__])
