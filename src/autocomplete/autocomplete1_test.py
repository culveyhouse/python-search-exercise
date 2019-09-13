import json
from os import path

from autocomplete1 import Autocomplete1
from suggestions import Suggestions

def testAutocomplete1():
    data = Suggestions.load()
    autocomplete = Autocomplete1(data)

    results = autocomplete.performSearch('biology')

    expectedPath = path.dirname(__file__) + '/expected/autocomplete1_expected.json'
    with open(expectedPath, 'r') as f:
        expected = json.load(f)

    assert len(results) == 15
    assert results[0] == expected
