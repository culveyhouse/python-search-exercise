import json
from os import path

from autocomplete2 import Autocomplete2
from suggestions import Suggestions

def testAutocomplete2():
    data = Suggestions.load()
    autocomplete = Autocomplete2(data)

    results = autocomplete.performSearch('Biology')

    expectedPath = path.dirname(__file__) + '/expected/autocomplete2_expected.json'
    with open(expectedPath, 'r') as f:
        expected = json.load(f)

    assert len(results) == 6
    assert results[0] == expected[0]
    assert results[4] == expected[1]
