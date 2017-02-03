
# ********************* #
# RecipeFinder project
# ********************* #

# First test for web crawling: this will be a combination of learning
# and dabbling with one url for crawling recipes relating to a specific keyword
# Python Version 3.5 / 2.7

# Script to find and parse html lnks
from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super.__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters
    # an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.link.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


# expand to diplay page or part o it - create its own class
class TextFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super.__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
