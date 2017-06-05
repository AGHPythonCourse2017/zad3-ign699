from newspaper import Article
from zad3.google import Query
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
import re
import os


class ArticleData:
    def __init__(self, url):
        self.url = url


    def parse(self):
        self.article = Article(self.url)
        self.article.download()
        self.article.parse()
        self.article.nlp()
        with open(os.path.dirname(__file__) + "/" + 'sources.json') as data_file:
            data = json.load(data_file)
        self.data = list(data.keys())

    def authorsearches(self):
        if len(self.article.authors) == 0:
            print("No authors! Suspicious")
        else:
            return self.article.authors

    def getdate(self):
        return self.article.publish_date

    def checksite(self):
        urls = []
        req = requests.get(self.url)
        toExtr = BeautifulSoup(req.text, "html.parser")
        links = [link.get('href') for link in toExtr.find_all('a')]
        links = [urlparse(link).hostname for link in links]
        links.append(urlparse(self.url).hostname)
        S1 = set(links)
        S2 = set(self.data)
        S3 = S1.intersection(S2)
        if len(S3) > 0:
            print("The site is or contains links to not credible sources!")
        else:
            print("This site seens to be a credible source!")

    def checktitle(self):
        title = self.article.title
        hasupper = self.checkhasupper(title)
        punctuation = self.checkpunctuation(title)
        if hasupper == 1 or punctuation == 1:
            print("Title might be a clickbait")
        else:
        	print("Title doesnt seem to be a clickbait")



    def checkhasupper(self, title):
        upperWords = 0
        for word in title:
            if word.isupper():
                upperWords += 1
        if upperWords > 0:
            return 1
        else:
            return 0

    def checkpunctuation(self, title):
        serc = re.search("(\?\?+)|(!!+)", title)
        if serc:
            return 1
        else:
            return 0


    def getkeywords(self):
        return self.article.keywords

    def getsum(self):
        query = Query(self.article.summary)
        query.parse()
        links = query.gettopresults()
        linkstoread = []
        data = set(self.data)
        for link in links:
            host = urlparse(link).hostname
            if host:
	            if host[0] == 'w':
	                host = host[4:]
	            comp = set()
	            comp.add(host)
	            if len(data.intersection(comp)) == 0:
	                linkstoread.append(link)
        print("Here are links to other sites concerning the same issue")
        print("\n".join(linkstoread))
