import json
from os import path

from paged_autocomplete_controller import PagedAutocompleteController

class TestPagedAutocompleteController(object):

    def testReturnFirstPageOfSuggestions(self):
        response = PagedAutocompleteController.index('biology', 15, None)

        assert len(response['result']) == 15

        # TODO: Add more validation for this test case.

    def testIndicateNextPageOfSuggestions(self):
        response = PagedAutocompleteController.index('biology', 15, None)

        assert response['status']['moreResults'] == True
        assert response['status']['pageNext'] == 2

    def testReturnSecondPageOfSuggestions(self):
        response = PagedAutocompleteController.index('biology', 15, 2)

        assert len(response['result']) == 14
        assert response['status']['moreResults'] == False
        # TODO: Add more validation for this test case.
