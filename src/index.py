import json
import logging
import os
import re
import SimpleHTTPServer
import SocketServer
from urlparse import urlparse, parse_qsl

from controllers.general_autocomplete_controller import GeneralAutocompleteController
from controllers.paged_autocomplete_controller import PagedAutocompleteController
from controllers.simple_autocomplete_controller import SimpleAutocompleteController

PORT = 9000
VIEWS_PATH = os.path.join(os.path.dirname(__file__), 'views/index.html')

# SimpleHTTPServer serves files from within the working
# directory so setting current working directory to be /views.
os.chdir(os.path.dirname(VIEWS_PATH))

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def _setResponse(self, content, contentType='application/json'):
        self.send_response(200)
        self.send_header('Content-type',  contentType)
        self.send_header("Content-length", len(content))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        parsedUrl = urlparse(self.path)
        queryParts = dict(parse_qsl(parsedUrl.query))

        if parsedUrl.path == '/':
            # This case is already handled by SimpleHTTPServer.
            pass
        elif parsedUrl.path == '/index':
            term = queryParts.get('searchTerm', None)
            self._setResponse(json.dumps(SimpleAutocompleteController.index(term)))
        elif parsedUrl.path == '/pagedindex':
            term = queryParts.get('searchTerm', None)
            count = int(queryParts.get('count', '15'))
            pageStart = queryParts.get('pageStart', None)
            self._setResponse(json.dumps(PagedAutocompleteController.index(term, count, pageStart)))
        elif parsedUrl.path == '/generalindex':
            query = queryParts.get('q', None)
            fields = queryParts.get('fields', None)
            count = int(queryParts.get('count', '15'))
            pageStart = queryParts.get('pageStart', None)
            self._setResponse(json.dumps(GeneralAutocompleteController.index(query, fields, count, pageStart)))
        else:
            self._setResponse('404: Page Not Found.', 'text/html')

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(('0.0.0.0', PORT), Handler)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    logger.info('Challenge server is listening on http://localhost:9000')
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
