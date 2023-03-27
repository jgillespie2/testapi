import json

import pytest


@pytest.fixture(scope='module')
def json_file():
    with open('Details.json') as details_json_file:
        json_contents = details_json_file.read()
        parsed_contents = json.loads(json_contents)
        yield parsed_contents