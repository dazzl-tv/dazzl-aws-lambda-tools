class Parameters:
    def __init__(self, environment):
        '''
        Constructor for this class.
        Create parameters dict.
        '''
        self.environment = environment


    def token(self):
        return {
            'username': self.environment.get_username(),
            'password': self.environment.get_password(),
            'grant_type': 'password'
        }


    def revoke(self, token):
        return {
            'username': self.environment.get_username(),
            'password': self.environment.get_password(),
            'token': token
        }
