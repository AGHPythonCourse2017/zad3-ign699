import unittest
from google import Query
from zad3 import ArticleData

class test(unittest.TestCase):
    def testQuery(self):
        links = ["https://www.google.pl/search?q=private+methods+python&oq=private+methods+python&aqs=chrome..69i57j0l5.4126j0j7&sourceid=chrome&ie=UTF-8"]
        self.assertEqual(Query.glinkton(self, links), ["https://www.google.pl/search?q=private+methods+python&"])

    def testzad3(self):
        self.assertEqual(ArticleData.checkhasupper(self, "asd ASD asd ASD"), 1)
        self.assertEqual(ArticleData.checkhasupper(self, "asd 111 asd 111"), 0)
        self.assertEqual(ArticleData.checkpunctuation(self, "This title is clickbait !!"), 1)
        self.assertEqual(ArticleData.checkpunctuation(self, "This title is not a clickbait!"), 0)
        self.assertEqual(ArticleData.checkpunctuation(self, "This title is clickbait ??"), 1)
        self.assertEqual(ArticleData.checkpunctuation(self, "This title is not a clickbait?"), 0)


if __name__ == '__main__':
    unittest.main()