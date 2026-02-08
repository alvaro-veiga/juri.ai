import requests
from urllib.parse import urlencode, urljoin
import os


EVOLUTION_API_BASE_URL = os.getenv('EVOLUTION_API_BASE_URL')
EVOLUTION_API_KEY = os.getenv('EVOLUTION_API_KEY')


class BaseEvolutionAPI:
    def __init__(self):
        self._BASE_URL = EVOLUTION_API_BASE_URL
        self._API_KEY = {
            "arcane": EVOLUTION_API_KEY
        }

    def _send_request(
        self,
        path,
        method='GET',
        body=None,
        headers=None,
        params_url=None
    ):
        if headers is None:
            headers = {}
        if params_url is None:
            params_url = {}
            
        method = method.upper()
        url = self._mount_url(path, params_url)
        
        headers.setdefault('Content-Type', 'application/json')
        instance = self._get_instance(path)
        headers['apikey'] = self._API_KEY.get(instance)

        request_method = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }.get(method)

        return request_method(url, headers=headers, json=body)
        
    def _mount_url(self, path, params_url):
        parameters = ""
        if isinstance(params_url, dict) and params_url:
            parameters = urlencode(params_url)
        
        url = urljoin(self._BASE_URL, path)

        if parameters:
            url = url + '?' + parameters
        return url
        
    def _get_instance(self, path):
        return path.strip('/').split('/')[-1]


class SendMessage(BaseEvolutionAPI):

    def send_message(self, instance, body):
        path = f'/message/sendText/{instance}/'
        return self._send_request(path, method='POST', body=body)