import urllib

# Required since Pytest and simple HTTP server do not handle relative paths the same
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from autocomplete.autocomplete3 import Autocomplete3
from autocomplete.suggestions import Suggestions

class GeneralAutocompleteController:
    @classmethod
    def index(cls, query, fields, count, pageStart):
        """Performs a case insensitive contains search on the given fields,
        optionally returning a subset of the suggestion objects in pages.

        Example:
            http://localhost:9000/generalindex?q=title:biology,attribution:raven&fields=title,subtitle,edition&count=20&pageStart=<pageKey>
        
        Args:
            query - the search query. This is a string of comma seperated
                    key/value pairs to filter the search on. For example, this
                    query string, 'title:biology,attribution:raven' should
                    search for books where the title contains 'biology' and
                    where the attribution field contains 'raven'.
            fields - the fields that should be returned. This is a string
                     of comma seperated fields(e.g. 'title,subtitle,edition')
            count -  the max number of results to return.
            pageStart - parameter to indicate where to start the page.

        Return:
            Dictionary containing the list of results that match the searchTerm
            and contain only the fields specified. Paging information should
            also be included in the dictionary. Return dictionary should
            include these fields in this format:

            {
                'status': {
                    'moreResults': <Boolean>
                    'pageNext': <String|Int>
                },
                'result': <List>
            }
        """

        search_dict = {} # dict to store the converted key:value search terms
        more_results = False # Boolean to indicate whether there are more results
        pageNext = None # Int to indicate the paging key for use with next page link
        if not pageStart:
            pageStart = 1 # E stablish human-readable "page 1" if no pagination yet

        # Decode any URL encoded characters in the searchTerm query string
        search_kv = query.split(',')
        for kv in search_kv:
            k,v = kv.split(':')
            v = urllib.unquote(v)
            search_dict[k]=v
        
        if fields:
            fields = fields.split(',')

        data = Suggestions.load() # load JSON data from data/suggestions.json
        
        # Autocomplete3 has all functionality necessary for this controller
        autocomplete = Autocomplete3(data) 
        
        """Get list of dictionary items up to max "count", as well as the 
        boolean moreResults which indicates whether more pages of results exist
        """
        results, more_results = autocomplete.performSearch(search_dict, count, 
            (pageStart-1)*count, fields)

        status = {'moreResults': more_results}
        
        # Add "pageNext" to status dict if the performSearch indicated more results
        if more_results: 
            status['pageNext'] = pageStart+1
        
        return_dict = {
            'status': status,
            'result': results
        }

        return return_dict
