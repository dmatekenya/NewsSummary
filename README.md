# NewsSummary
A simple script which harvests news articles from a website of interest (for example: http://www.nyasatimes.com) and then summarises all articles in a word cloud.
#Contents
In this project I have a *news_crawler.py* script which harvest articles from a news website hardcoded in the script. 
The articles are saved in a folder. The second piece of code is an R script *word_cloud.R* which takes all the articles and creates a word cloud.

#References
I got inspiration and some code from these wonderful previous works:

1. http://www.sthda.com/english/wiki/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know

  After an unsuccessful attempt to find an easy way to create a word cloud in Python, I decided to do it in R and the blog above..
  helped me alot with the process because I have gone a little rusty in suign R.
  
2.http://code.runnable.com/UqqXuSGIpqAeAAPR/how-to-make-a-web-crawler-for-python-and-requests

    I modified code from link above to create a simple crawler after I had a little fall out with Scrapy. 
