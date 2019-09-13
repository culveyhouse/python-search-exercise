import json
from os import path

from autocomplete3 import Autocomplete3
from suggestions import Suggestions

def testAutocomplete3():
    data = Suggestions.load()
    autocomplete = Autocomplete3(data)

    results = autocomplete.performSearch('BIOLOGY')

    expectedPath = path.dirname(__file__) + '/expected/autocomplete3_expected.json'
    with open(expectedPath, 'r') as f:
        expected = json.load(f)

    assert len(results) == 29
    assert results[1] == expected[0]
    assert results[3] == expected[1]
