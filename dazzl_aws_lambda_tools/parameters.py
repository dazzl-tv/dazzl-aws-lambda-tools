class Parameters:
    def __init__(self, environment):
        '''
        Constructor for this class.
        Create parameters dict.
        '''
        self.environment = environment


    def token(self):
        '''
        Prepare body for request create token.

        >>> import os
        >>> from environment import Environment
        >>> os.environ['USERNAME_DEVE'] = 'roger@dazzl.local'
        >>> os.environ['PASSWORD_DEVE'] = 'yopyopy'
        >>> env = Environment('my.bucket.name.development')
        >>> Parameters(env).token()
        {'username': 'roger@dazzl.local', 'password': 'yopyopy', 'grant_type': 'password'}
        '''
        return {
            'username': self.environment.get_username(),
            'password': self.environment.get_password(),
            'grant_type': 'password'
        }


    def revoke(self, token):
        '''
        Prepare body for request revoke token.

        >>> import os
        >>> from environment import Environment
        >>> env = Environment('my.bucket.name')
        >>> os.environ['USERNAME_PROD'] = 'roger@dazzl.local'
        >>> os.environ['PASSWORD_PROD'] = 'yopyop'
        >>> Parameters(env).revoke('SuperToken')
        {'username': 'roger@dazzl.local', 'password': 'yopyop', 'token': 'SuperToken'}
        '''
        return {
            'username': self.environment.get_username(),
            'password': self.environment.get_password(),
            'token': token
        }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
