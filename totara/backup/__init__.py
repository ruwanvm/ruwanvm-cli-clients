import requests


class Backup:
    def __init__(self, api_url):
        self.api_url = f"{api_url}/backup"

    def status(self, backup_id):
        response = requests.get(f"{self.api_url}/status/{backup_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
