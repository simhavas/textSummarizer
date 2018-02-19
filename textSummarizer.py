# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 06:17:06 2018

@author: simha
"""

# get url to summarize
import urllib2
from bs4 import BeautifulSoup
from frequencySummarizer import FrequencySummarizer


def get_only_text_from_url(url,tag):
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,'html.parser')
    
    text = ' '.join(map(lambda p: p.text, soup.find_all(tag)))
    text = ' '.join(map(lambda p: p.text.encode("ascii", 'ignore'), soup.find_all('p')))
    
    return soup.title.text, text



# Testing
#url = 'https://www.washingtonpost.com/news/politics/wp/2018/02/18/they-are-laughing-their-asses-off-in-moscow-trump-takes-on-the-fbi-russia-probe-and-2016-election/?hpid=hp_hp-top-table-main_trump-tweets-930am%3Ahomepage%2Fstory&utm_term=.4ca83bff1215'

url = 'http://www.thehindu.com/news/national/other-states/maoists-kill-three-in-chhattisgarh/article22791486.ece'
tag = ('div',{'class':'article'})
textOfurl = get_only_text_from_url(url,tag)

fs = FrequencySummarizer()
summary = fs.summarize(textOfurl[1], 3)