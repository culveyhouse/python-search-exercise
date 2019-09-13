# Inkling Python Code Challenge

This code challenge is designed to mirror real world tasks that we do in relation to search and APIs here at Inkling. Each challenge builds on the other, taking you through a progression of prototyping to a more robust solution for creating an autocomplete backend in Python.

### Getting started

You will need to install dependencies by running:

```sh
pip install -r requirements.txt
```

This challenge uses Python's [SimpleHTTPServer module](https://docs.python.org/2/library/simplehttpserver.html) to implement a basic API. For testing it uses [pytest](https://docs.pytest.org/en/latest/getting-started.html).

### Taking the Challenge

We've added a number of stub files and tests, each representing a task to complete. Each task has one or more unittests associated with them. You can run all the tests by running:

```sh
pytest
```

To start the web server for the controller challenges, run:

```sh
python src/index.py
```

The three API endpoints implemented here are [index](http://localhost:9000/index), [pagedindex](http://localhost:9000/pagedindex), and [generalindex](http://localhost:9000/generalindex).

Note: The web server does not pick up live changes, restart the web server to get changes out.

### Sample Data

Sample book data has been provided in the [suggestions.json](src/data/suggestions.json) file and a utility in [suggestions.py](src/autocomplete/suggestions.py) has been provided to easily get that list of data from it. Most of the unit tests already make use of this data and you should avoid making modifications to it.

### The Rules

Feel free to research information on the internet or use additional libraries as long as the task is not implemented for you.

We've put a number of tasks into this challenge and do not expect folks to finish every single challenge. Take your time and work through each one, ensuring that your code is well structured, documented if necessary, and well tested. Commit your code changes to the repository after completing each challenge. Complete the tasks in the order:

1. [Autocomplete1](src/autocomplete/autocomplete1.py)
2. [Autocomplete2](src/autocomplete/autocomplete2.py)
3. [Autocomplete3](src/autocomplete/autocomplete3.py)
4. [SimpleAutocompleteController](src/controllers/simple_autocomplete_controller.py)
5. [PagedAutocompleteController](src/controllers/paged_autocomplete_controller.py)
6. [GeneralAutocompleteController](src/controllers/general_autocomplete_controller.py)

If you do complete all the tasks, feel free to add additional endpoints and controllers to the server to experiment with other improvements that could be made to this system. Feel free to use docker and docker-compose if you want to expore using other services like Elasticsearch.

If you have further thoughts on how to improve the code base in the long term, please include a new FUTURE_IMPROVEMENTS.md with your recommendations.

### Finishing Up

When you are completed with the challenge, please zip up the repository and send it back over email. Please note the amount of time you took.