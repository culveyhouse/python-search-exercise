import json
from os import path

from simple_autocomplete_controller import SimpleAutocompleteController

def testSimpleAutocompleteController():
    response = SimpleAutocompleteController.index('biology')
    assert len(response['result']) == 29

    # TODO: Add more validation for this test case.
