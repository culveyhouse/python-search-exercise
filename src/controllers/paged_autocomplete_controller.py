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
            pageStart - parameter to indicate where to start the page.

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
        # TODO: Implement this.
        return {
            'status': {},
            'result': []
        }
