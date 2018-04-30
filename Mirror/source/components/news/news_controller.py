class NewsController:
    def __init__(self, parser):
        self.parser = __import__(f'source.components.news.services.{parser}.{parser}', fromlist=['Parser']).Parser()

    def current_news(self, news_type):
        return self.parser.current_news(news_type)
