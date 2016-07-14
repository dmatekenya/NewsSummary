#A simple crawler to retrieve news articles

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import datetime
import os

#Takes a link, extracts the required core text of an article
#and finally writes to file, with the article title as
#file name
def get_text_from_html(url,title,out_dir):
    print ('Downloading: %s'%url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get only div with text-I had to manualy go through the website to be
    #able to know ehich tag to use for article content
    #In this case, all divs with class 'entry-content gave me pretty much the content I wanted
    div = soup.find_all('div', {'class': 'entry-content'})
    #List to hold all paragraph text from each paragraph in the div
    out_text = [title]
    for p in div:
        out_text.append(p.text)

    #Now write tjhe contents to file
    file_name = out_dir+title+'.txt'
    f = open(file_name,mode='w')

    #We dont write if contents are too few, probably not a legitimate article
    print (len(out_text))

    if len(out_text) ==1:
        return
    #write each line to file
    #first line is title
    for item in out_text:
        f.write("%s\n" % item)


def crawl(url, maxlevel, out_dir):
    #Now I dont have a bterr way but I simply want to skip all titles with
    #words such as Google because they arent true articles
    skip_list=['Twitter','Facebook', 'Google', 'LinkedIn']

    # Limit the recursion, we're not downloading the whole Internet
    if(maxlevel == 0):
        return

    # Get the webpage
    req = requests.get(url)
    soup = BeautifulSoup(req.content)

    # Check if successful
    if(req.status_code != 200):
        return []

    # Find and follow all the links
    links = {}
    for x in soup.find_all('a'):
        if x.has_attr('title'):
            links[x['title']] = x['href']

    for title,link in links.items():
        #skip these
        skip = False
        for s in skip_list:
            if s in title:
                skip = True
                break

        if skip:
            continue
        # Get an absolute URL for a link
        try:
            get_text_from_html(link, title, out_dir)
            #print(text)
            crawl(link, maxlevel - 1, )
        except:
            continue

#The plan is to harvest articles everyday, hence use of date to create folder
now = datetime.datetime.now()
date = str(now.strftime("%Y-%m-%d"))
out_root_dir = '/Users/dmatekenya/PycharmProjects/WebMining/NewsClassifier/nyasa_times/'+date+'/'
newpath = out_root_dir
if not os.path.exists(newpath):
    os.makedirs(newpath)

#Finally we crawl
crawl('http://www.nyasatimes.com', 2, out_root_dir )
