import os
import json

class Database(object):
    def __init__(self, filename):
        f = open(filename, 'rb')
        json_data = f.read()
        self.data = json.loads(json_data)

    def get(self, **kwargs):
        results = []
        for key, value in kwargs.items():
            for city in self.data:
                if city.get(key) == value:
                    results.append(city)
        results.sort(key=lambda c: c['population'], reverse=True)
        return results


class Cities(Database):
    pass

DATABASE_DIR = os.path.join(os.path.dirname(__file__), 'databases')
cities = Cities(os.path.join(DATABASE_DIR, 'cities.json'))
