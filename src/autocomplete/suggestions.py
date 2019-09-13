import json
import os

SUGGESTIONS_PATH = os.path.join(
    os.path.dirname(__file__), '../../data/suggestions.json'
)

class Suggestions:
    @classmethod
    def load(cls):
        with open(SUGGESTIONS_PATH, 'r') as f:
            return json.load(f)['data']
