from .environment import Environment
from .logger import Logger
from .request import Request

class Lambda:
    env = ''
    bucket = ''
    logger = None


    def __init__(self, bucket):
        '''
        Constructor for this class.
        Initialize environment and level log for lambda function.
        '''
        self.env = Environment(bucket)
        self.logger = Logger(self.env)
        self.logger.info_about_lambda(self.env)

        if (self.env.get_api_endpoint() != None):
            self.logger.info_about_requester(self.env)
            self.request = Request(self.env)


    def env(self):
        '''
        Return current environment.
        '''
        return self.env.name


    def bucket_name(self):
        '''
        Return name to bucket used by lambda function
        '''
        return self.bucket


    def send_request(self, verb, path, body):
        '''
        Send request to API.
        '''
        self.request.send(verb, path, body)
