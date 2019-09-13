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
        # TODO: Implement this.
        return {
            'result' : []
        }
