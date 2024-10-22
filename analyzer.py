# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
# from vaderSentiment import SentimentIntensityAnalyzer

import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Provide a valid email ('de' parameter), where we can reach you in case of troubles, 
# and enjoy 50000 chars/day


class Analyzer:
    def translate(self,originLang=None,to=None,sentence=None,email=None):
        if (originLang == None or to==None or sentence==None or email==None ):
            raise Exception("All values must be provided")

        url = f"https://api.mymemory.translated.net/get"
        params = {"q":sentence,"langpair":f"{originLang}|{to}","de":email}
        return requests.get(url,params).json()

    def sentiment_analyzer(self,sentence, analyzer):
        vs = analyzer.polarity_scores(sentence)
        print("{:-<30} {}".format(sentence,str(vs)))
        return vs

    def analyze(self,sentence, originLang):
        if (originLang != "en"):
            sentence = self.translate(originLang, "en", sentence,"yostinlds10yt@gmail.com")["responseData"]["translatedText"]
        return self.sentiment_analyzer (sentence,SentimentIntensityAnalyzer())
    

