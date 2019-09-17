import re

class Autocomplete3:
    def __init__(self, suggestions):
        self.suggestions = suggestions

    def performSearch(self, term, limit=None, offset=None):
        """Searches through the possible suggestions, creating an array of
        matches for any books whose title matches the specified search term.

        This method performs a case insensitive contains search and sort the
        results by title. Additionally, it takes two optional parameters for
        paginated results, limit and offset. Limit (also called count in 
        other classes) is the maximum number of results to return, and offset 
        denotes the number of records to pop from the sorted list of 
        dictionaries from the start of the list. 

        Example:
            With 'BIOLOGY' specified as the term a book with the title
            'Biology' should be returned. A book with the title 'Microbiology'
            should also be returned.

        Args:
            term = the term to search for in book titles.
            limit = maximum number of autocomplete suggestions to return 
            offset = number of dictionary entries to pop/ignore from list start
            (Note: limit and offset must be passed together, or neither)

        Return:
            List of results (dictionary entries) where the title contains 
            the search term.
        """

        # If limit or offset is passed, both must be present
        if (offset is None) is not (limit is None):
            raise Exception("Autocomplete3.performSearch Error: You must pass " 
            "an offset and limit, or neither")
            
        # A list of dictionary entries that match the "term" argument
        results = [] 
        
        # Compiled case-insensitive regex search using "term" argument for efficiency
        term_search = re.compile(r"{}".format(term), re.I) 

        # Boolean to return whether there are more paginated results beyond limit
        truncated = False

        for suggestion in self.suggestions:
            # Our suggestions may contain special UTF-8 characters
            title = suggestion['title'].encode("utf-8")
            if term_search.search(title): 
                results.append(suggestion)

        sorted_results = sorted(results, key = lambda suggestion: suggestion['title'])

        # Handle pagination / truncation if limit & offset were passed
        if offset>=0 and limit:
            # Check if remaining entries after offset are more than max per page
            if len(sorted_results[offset:])>limit:
                truncated = True
            # The transformed slice of sorted results for the current page
            sorted_results = sorted_results[offset:(offset+limit)]

        """Return only list of sorted_results unless the list was truncated by 
        limit/offset arguments, in which case indicate whether there was a 
        remainder that was truncated 
        """
        return (sorted_results, truncated) if offset>=0 else sorted_results  