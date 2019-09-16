import re

class Autocomplete1:
    def __init__(self, suggestions):
        self.suggestions = suggestions

    def performSearch(self, term, limit=None):
        """Searches through the possible suggestions, creating an array of
        matches for any books whose title matches the specified search term.

        This should perform a case sensitive contains search.

        Example:
            With 'biology' specified as the term a book with the title
            'Microbiology' should be returned. A book with the title 'Biology'
            should not be returned.

        Args:
            term = the term to search for in book titles.
            limit = maximum number of autocomplete suggestions to return 

        Return:
            List of results (dictionary entries) where the title contains 
            the search term.
        """
        
        # A list of dictionary entries that match the "term" argument
        results = [] 

        # Compiled regex search using "term" argument for efficiency
        term_search = re.compile(r"{}".format(term)) 

        for suggestion in self.suggestions:
            # Our suggestions may contain special UTF-8 characters            
            title = suggestion['title'].encode("utf-8")
            if term_search.search(title): 
                results.append(suggestion)
                
                # Limit autocomplete results if limit passed
                if limit and len(results)>=limit: 
                    break

        return results
