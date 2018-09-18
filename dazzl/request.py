import requests
import logging
import json

from .parameters import Parameters
from .headers import Headers

class Request:
    def __init__(self, env):
        '''
        Constructor for class Request.
        Initialize requester used by Lambda script.
        '''
        self.environment = env
        self.parameters = Parameters(self.environment)
        self._oauth_token()


    def __del__(self):
        '''
        Destroy automatically token in backend.
        '''
        self._oauth_revoke()


    def send(self, verb, path, body={}):
        '''
        Build request and send.
        If you use environment development write request in logger.
        '''
        try:
            header = Headers()

            if verb.upper() == 'POST':
                requests.post(path, json=body, verify=False,
                            headers=header.oauth())
            elif verb.upper() == 'GET':
                requests.get(path, json=body, verify=False,
                             headers=header.oauth())
            elif verb.upper() == 'PUT' or verb.upper() == 'PATCH':
                requests.put(path, json=body, verify=False,
                             headers=header.oauth())
            elif verb.upper() == 'DELETE':
                requests.delete(path, json=body, verify=False,
                                headers=header.oauth())
        except requests.exceptions.MissingSchema as e:
            logging.critical('URL to API is not correctly configured !')
            logging.critical('Request [{}] not sending !'.format(path))
            logging.critical(e)


    def _path_oauth_token(self):
        '''
        Path for ask token to Dazzl service
        '''
        return '{}/oauth/token'.format(self.environment.get_api_endpoint())


    def _path_oauth_revoke(self):
        '''
        Path for revoke token to Dazzl service.
        '''
        return '{}/oauth/revoke'.format(self.environment.get_api_endpoint())


    def _oauth_token(self):
        '''
        Send request to backend for ask valid token.
        '''
        try:
            response = requests.post(self._path_oauth_token(),
                                     json=self.parameters.token(),
                                     headers={},
                                     verify=False)
            data = json.loads(response.text)
            self.access_token = data['access_token']
            self.refresh_token = data['refresh_token']
            self.type_token = data['token_type']
        except requests.exceptions.MissingSchema as e:
            logging.critical('URL to API is not correctly configured !')
            logging.critical('Token creation failed !')
            logging.critical(e)


    def _oauth_revoke(self):
        '''
        Send request to backend for ask to revoke token.
        '''
        try:
            requests.post(self._path_oauth_revoke(),
                          json=self.parameters.revoke(self.access_token),
                          headers={},
                          verify=False)
        except requests.exceptions.MissingSchema as e:
            logging.critical('URL to API is not correctly configured !')
            logging.critical('Token revokation failed !')
            logging.critical(e)
