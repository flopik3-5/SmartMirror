class News:
    def __init__(self, title, url, body=None):
        self.title = title
        self.body = body
        self.url = url

    def __str__(self):
        return f'{self.title}.\n{self.body}'
