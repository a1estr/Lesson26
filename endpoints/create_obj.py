import requests
from dateutil.parser import isoparse
from endpoints.base_endpoint import Endpoint


class CreateObj(Endpoint):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"},
                    "price": {"type": "number"},
                    "CPU model": {"type": "string"},
                    "Hard disk size": {"type": "string"}
                },
                "required": ["year", "price", "CPU model", "Hard disk size"]
            },
            "createdAt": {"type": "string"}
        },
        "required": ["id", "name", "data", "createdAt"]
    }

    def new_obj(self, payload):
        self.response = requests.post(f'{self.url}/objects',
                                      json=payload)
        self.response_json = self.response.json()

    def get_name(self):
        return self.get_data()['name']

    def get_id(self):
        return self.get_data()['id']

    def get_create_time(self):
        create_time = self.get_data()['createdAt']
        dt = isoparse(create_time)
        return dt.replace(microsecond=0).isoformat()
