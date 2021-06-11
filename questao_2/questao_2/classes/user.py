import jwt


class User:

    def __init__(self, *args):
        self.jwt = jwt.JWT()
        self.user = args

    def populate_user(self, *args):
        self.user = args[0]

    def get_access_token(self, value):
        access_token = [c for c in value if "accesstoken" in str(c)]
        access_token_jwt = self.jwt.decode(access_token[0].__str__().split('=')[1].split(';')[0], None, None)
        return access_token_jwt['token']
