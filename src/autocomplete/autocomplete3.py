import re

class Autocomplete3:
    def __init__(self, suggestions):
        self.suggestions = suggestions

    def performSearch(self, terms, limit=None, offset=None, fields=None):
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
            term (str or dict): the term/terms to search for in book suggestions. 
            limit = maximum number of autocomplete suggestions to return 
            offset = number of dictionary entries to pop/ignore from list start
            (Note: limit and offset must be passed together, or neither)
            fields = an optional subset of dictionary keys to return for each result

        Return:
            List of results (dictionary entries) where the title contains 
            the search term, and 
            truncated (bool): Optionally returned if pagination exists and more
            results are queued beyond the results returned
        """

        # If limit or offset is passed, both must be present
        if (offset is None) is not (limit is None):
            raise Exception("Autocomplete3.performSearch Error: You must pass " 
                "an offset and limit, or neither")
            
        # A list of dictionary entries that match the "term" argument
        results = [] 
        term_search = {} # A dictionary of regex compilers for each search field
        
        # Detect whether one term is used instead of an entire query dictionary
        if type(terms) is str:
            terms = {'title':str(terms)}

        # Compile a case-insensitive regex search for each search term
        for k, v in terms.iteritems():
            terms[k] = repr(v) # To convert integers to strings and other normalization
            term_search[k] = re.compile(r"{}".format(v), re.I)

        # Boolean to return whether there are more paginated results beyond limit
        truncated = False

        # Now crawl though all book suggestions and attempt to match query string to each
        for suggestion in self.suggestions:
            match_fail = False # A flag to detect any failed match in each suggestion
            for key, search in term_search.iteritems():
                '''Try to match each query term via regex to the suggestion's key
                of the same name.
                Our suggestions may contain special UTF-8 characters and may
                be an integer type, so we must use repr and encode functions
                '''
                suggestion_value = repr(suggestion[key]).encode("utf-8")
                # If any search fails in one suggestion, then move on
                if not term_search[key].search(suggestion_value):
                    match_fail = True
                    continue
            if not match_fail:
                results.append(suggestion) # continue building matched results

        # Regardless of search and field criteria, always sort results against title
        sorted_results = sorted(results, key = lambda suggestion: suggestion['title'])

        # Handle pagination / truncation if limit & offset were passed
        if offset>=0 and limit:
            # Check if remaining entries after offset are more than max per page
            if len(sorted_results[offset:])>limit:
                truncated = True
            # The transformed slice of sorted results for the current page
            sorted_results = sorted_results[offset:(offset+limit)]

        # Return only a subset of the total fields of each dict entry if specified
        if fields:
            subset_results = [] # This list will store the subset fields of sorted_results
            for entry in sorted_results:
                this_subset = {} # Temporary dict re-used with each iteration
                for k,v in entry.iteritems():
                    if k in fields:
                        this_subset[k] = v
                subset_results.append(this_subset)
            sorted_results = subset_results
            del subset_results
        
        """Return only list of sorted_results unless the list was truncated by 
        limit/offset arguments, in which case indicate whether there was a 
        remainder that was truncated 
        """
        return (sorted_results, truncated) if offset>=0 else sorted_results  
        