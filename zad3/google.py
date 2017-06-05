import requests
from bs4 import BeautifulSoup
import re


class Query:
    def __init__(self, searchTerm):
        self.term = searchTerm

    def parse(self):
        self.req = requests.get("https://www.google.com/search?q=" + self.term)
        self.toExtr = BeautifulSoup(self.req.text, "html.parser")

    def gettopresults(self):
        links = self.toExtr.select('.r a')
        links = [link.get('href') for link in links]
        links = self.glinkton(links)
        links = [link[:-1] for link in links]
        return links

    def glinkton(self, links):
        return [re.search("(www.)|(http).+?&", link).group(0) for link in links]