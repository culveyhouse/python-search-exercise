import json
from os import path

from general_autocomplete_controller import GeneralAutocompleteController

class TestGeneralAutocompleteController(object):

    def testPageSimpleCase(self):
        response = GeneralAutocompleteController.index('title:biology', None, 15, None);

        assert len(response['result']) == 15
        assert response['status']['moreResults'] == True

    def testSupportAComplexQuery(self):
        response =  GeneralAutocompleteController.index(
            'title:biology,attribution:raven',
            None,
            15,
            None
        );

        assert len(response['result']) == 1
        assert response['status']['moreResults'] == False

    def testReturnOnlySelectedFields(self):
        response = GeneralAutocompleteController.index(
            'title:biology,attribution:raven',
            'publisher,price',
            15,
            None
        )

        assert len(response['result']) == 1

        # TODO: Add more validation for this test case.
