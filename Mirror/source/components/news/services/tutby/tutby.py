import jsonpickle
import os
from pyquery import PyQuery
from source.components.news.news import News


class Parser:
    def __init__(self):
        self.file = jsonpickle.decode(open(f'{os.path.dirname(__file__)}\\news_type_ids.json', 'r').read())
        self.url = "http://tut.by"

    def current_news(self, news_type):
        type_id = self.news_type_to_id(news_type)
        page = PyQuery(self.url)
        news = []
        raw_news = PyQuery(page)(f'#{type_id} a.entry__link.io-block-link')
        for i in range(0, raw_news.__len__()):
            temp = News(PyQuery(raw_news[i])("span.entry-head._title").text(),
                        PyQuery(raw_news[i]).attr("href"))
            news.append(self.fill_news_body(temp))
        return page(f'#{type_id}').attr("data-io-title"), list(filter(lambda x: x.body is not "", news))

    def news_type_to_id(self, news_type):
        return self.file[news_type]

    @staticmethod
    def fill_news_body(news):
        news.body = PyQuery(news.url)("#article_body strong").text()
        return news
