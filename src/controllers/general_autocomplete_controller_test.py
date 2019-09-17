import json
from os import path

from general_autocomplete_controller import GeneralAutocompleteController

class TestGeneralAutocompleteController(object):

    def testPageSimpleCase(self):
        response = GeneralAutocompleteController.index(
            'title:biology', 
            None, 
            15, 
            None);

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

    # Additional test added by Daniel Culveyhouse to validate pagination 
    def testReturnPaginatedSelectedFields(self):
        response = GeneralAutocompleteController.index(
            'primaryCategory:business,copyrightYear:2012',
            'edition,title,primaryCategory,copyrightYear',
            5,
            2
        )
        
        expectedPath = path.dirname(__file__) + '/expected/general_autocomplete_controller_expected.json'
        with open(expectedPath, 'r') as f:
            expected = json.load(f)
        
        assert len(response['result']) == 5
        assert response['result'] == expected

        # TODO: Add more validation for this test case.
