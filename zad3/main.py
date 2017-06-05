from zad3.art3 import ArticleData

def checkart(link):
	article = ArticleData(link)
	article.parse()
	print("First check the date if its older than one month you should get suspicious")
	print(article.getdate())
	article.checksite()
	article.checktitle()
	article.getsum()
