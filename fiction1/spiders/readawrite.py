import scrapy

from .togetList import genList
from ..items import FictionItem


class readawrite(scrapy.Spider):
    name = 'readawrite'
    domain = 'https://www.readawrite.com/a/a'
    link = ""
    object1 = genList()
    story = object1.methodA()

    def start_requests(self):
        #print(self.story)
        for i in self.story:
            link = str(self.domain) + str(i)
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        items = FictionItem()

        title = response.xpath("//script[contains(., 'var article_name')]/text()").re(
            r"var article_name = '(.+?)'.replace")
        author = response.xpath("//script[contains(., 'var author_name')]/text()").re(
            r"var author_name = '(.+?)'.replace")
        category = response.xpath("//script[contains(., 'var category_name')]/text()").re(
            r"var category_name = '(.+?)';")
        tag = response.xpath("//meta[@property='article:tag']/@content").extract()
        description = response.xpath("//meta[@name='description']/@content").extract()
        isComplete = response.xpath("//span[@id='cover_end_text']/text()").extract()
        pic = response.xpath("//script[contains(., 'var article_thumbnail_path')]/text()").re(
            r"var article_thumbnail_path = '(.+?)';")
        viewer = response.xpath("//script[contains(., 'var view_count_full')]/text()").re(
            r"var view_count_full = '(.+?)';")
        numOfchap = response.xpath("//script[contains(., 'var chapter_count')]/text()").re(
            r"var chapter_count = '(.+?)';")
        commentCount = response.xpath("//script[contains(., 'var comment_count_full')]/text()").re(
            r"var comment_count_full = '(.+?)';")
        favouriteCount = response.xpath("//script[contains(., 'var favorite_count_full')]/text()").re(
            r"var favorite_count_full = '(.+?)';")
        ratingCount = response.xpath("//script[contains(., 'var rating_count_full')]/text()").re(
            r"var rating_count_full = '(.+?)';")
        url = response.request.url

        items['title'] = title
        items['author'] = author
        items['tag'] = tag
        items['description'] = description
        items['category'] = category
        items['isComplete'] = isComplete
        items['pic'] = pic
        items['viewer'] = viewer
        items['numOfchap'] = numOfchap
        items['commentCount'] = commentCount
        items['favouriteCount'] = favouriteCount
        items['ratingCount'] = ratingCount
        items['url'] = url

        yield items