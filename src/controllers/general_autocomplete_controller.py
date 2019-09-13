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
        # TODO: Implement this.
        return {
            'status': {},
            'result': []
        }
