import os


class Environment:
    def __init__(self, bucket_name):
        '''
        Constructor for class Environment.
        Initialize environment used by Lambda script.
        '''
        if 'development' in bucket_name:
            self.environment = 'development'
        elif 'staging' in bucket_name:
            self.environment = 'staging'
        else:
            self.environment = 'production'


    def name(self):
        '''
        Get name environment used
        '''
        return self.environment


    def development(self):
        '''
        Environment development ?
        '''
        return self.environment == 'development'


    def staging(self):
        '''
        Environment staging ?
        '''
        return self.environment == 'staging'


    def production(self):
        '''
        Environment production ?
        '''
        return self.environment == 'production'


    def  get_username(self):
        '''
        Read environment variable for username (email).
        '''
        return os.getenv('USERNAME_{}'.format(self._suffix_env()))


    def get_password(self):
        '''
        Read environment variable for password.
        '''
        return os.getenv('PASSWORD_{}'.format(self._suffix_env()))


    def get_api_endpoint(self):
        '''
        Read environment variable for API endpoint.
        '''
        return os.getenv('URL_API_{}'.format(self._suffix_env()))


    def _suffix_env(self):
        '''
        Get suffix for environment used by Lambda script.
        '''
        if (self.development):
            return 'DEVE'
        elif (self.staging):
            return 'STAG'
        elif (self.production):
            return 'PROD'


    # Aliases method
    dev = development
    prod = production
