class Bucket:
    def __init__(self, record):
        '''
        Constructor for this class.
        Initialize important bucket data.
        '''
        self.record = record


    def name(self):
        '''
        Read record and extract name to bucket.
        '''
        return self.record['s3']['bucket']['name']


    def key(self):
        '''
        Read record and extract key to bucket.
        '''
        return self.record['s3']['object']['key']
