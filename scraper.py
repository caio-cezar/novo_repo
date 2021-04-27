import newspaper
import nltk

site = newspaper.build('https://g1.globo.com/')

article = site.articles[1]

article.download()

article.parse()

nltk.download('punkt')

article.nlp()

article.summary()

article.text

    
