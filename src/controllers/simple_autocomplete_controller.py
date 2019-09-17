import urllib

# Required since Pytest and simple HTTP server do not handle relative paths the same
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from autocomplete.autocomplete3 import Autocomplete3
from autocomplete.suggestions import Suggestions

class SimpleAutocompleteController:
    @classmethod
    def index(cls, searchTerm):
        """Performs a case insensitive contains search on book titles.

        Example:
            http://localhost:9000/index?searchTerm=biology

        Args:
            searchTerm - the term to search for.

        Return:
            Dictionary containing the list of results that match the
            searchTerm. Return dictionary should be structured like so:

            {
                'result': <List>
            }
        """

        # Decode any URL encoded characters in the searchTerm query string
        searchTerm = urllib.unquote(searchTerm)
        
        data = Suggestions.load() # load JSON data from data/suggestions.json
        
        # Autocomplete3 has all functionality necessary for this controller
        autocomplete = Autocomplete3(data) 
        results = autocomplete.performSearch(searchTerm)
        return {
            'result' : results
        }
