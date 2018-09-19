class Headers:
    def __init__(self):
        '''
        Constructor for this class.
        Create headers dict.
        '''


    def oauth(self, token):
        return {
            'Content-Type': 'application/json',
            'Authorizations': 'Bearer '+token
        }
