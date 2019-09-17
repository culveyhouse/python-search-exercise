import urllib

# Required since Pytest and simple HTTP server do not handle relative paths the same
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from autocomplete.autocomplete3 import Autocomplete3
from autocomplete.suggestions import Suggestions

class PagedAutocompleteController:
    @classmethod
    def index(cls, searchTerm, count, pageStart):
        """Performs a case insensitive contains search on book titles,
        returning paged results.

        For the paging technique use any technique you would like. Feel free to
        use whatever kind of pageStart you think makes sense. The requirements
        on paging is that:
        - When there are more results beyond the current page the response
          contains "moreResults": true in the status object of the response. If
          there are no more results, "moreResults" should be false.
        - When there are more results beyond the current page the response
          contains a paging key in the "pageNext" field of the "status" object
          of the response. That paging key can then be passed as the pageStart
          url parameter to get the next page of results.

        Example:
            http://localhost:9000/pagedindex?searchTerm=biology&count=20&pageStart=<pageKey>

        Args:
            searchTerm - the term to search for.
            count - the max number of results to return.
            pageStart - int to indicate which "page" to continue page results

        Return:
            Dictionary containing the list of results that match the
            searchTerm as well as the paging information. Return dictionary
            should include these fields in this format:

            {
                'status': {
                    'moreResults': <Boolean>
                    'pageNext': <String|Int>
                },
                'result': <List>
            }
        """
        
        more_results = False # Boolean to indicate whether there are more results
        pageNext = None # Int to indicate the paging key for use with next page link
        if not pageStart:
            pageStart = 1 # Establish human-readable "page 1" if no pagination yet
        # Decode any URL encoded characters in the searchTerm query string
        searchTerm = urllib.unquote(searchTerm)       
        
        data = Suggestions.load() # load JSON data from data/suggestions.json
        
        # Autocomplete3 has all functionality necessary for this controller
        autocomplete = Autocomplete3(data) 
        
        """Get list of dictionary items up to max "count", as well as the 
        boolean moreResults which indicates whether more pages of results exist
        """
        results, more_results = autocomplete.performSearch(searchTerm, count, (pageStart-1)*count)

        status = {'moreResults': more_results}
        
        # Add "pageNext" to status dict if the performSearch indicated more results
        if more_results: 
            status['pageNext'] = pageStart+1
        
        return_dict = {
            'status': status,
            'result': results
        }

        return return_dict
