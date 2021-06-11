class header:

    def __init__(self, user, token):
        self.user = user
        self.token = token

    @property
    def header_mount(self):
        return {
            'Content-Type': 'application/json',
            'Loggeduser': self.user,
            'Accesstoken': self.token
        }
