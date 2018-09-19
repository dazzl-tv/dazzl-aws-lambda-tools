import logging
import os

class Logger:
    def __init__(self, environment):
        '''
        Constructor for class Logger.
        Initialize logger used by Lambda script.
        '''
        if (os.getenv('LOG_LEVEL')):
            self.level = self.eval_log_level()
        else:
            if environment.development:
                self.level = logging.DEBUG
            elif environment.staging:
                self.level = logging.INFO
            elif environment.production:
                self.level = logging.ERROR

        self.log = logging.getLogger()
        self.log.setLevel(self.level)


    def eval_log_level():
        '''
        Transform string in logging level.
        '''
        return eval('logging.{}'.format(os.getenv('LOG_LEVEL').upper()))


    def info_about_lambda(self, env):
        '''
        Write info in log to lambda (cloudwatch)
        '''
        self.log.log(self.level,
                     'Environment [{}] and logger [{}] configured, ' \
                     'execute Lambda function.'.format(env.name(),
                                                       logging.getLevelName(self.level)))


    def info_about_requester(self, env):
        '''
        Write info about requester configured
        '''
        self.log.log(self.level,
                     'URL API Endpoint configured [{}] with user [{}]'
                     .format(env.get_api_endpoint(), env.get_username()))
