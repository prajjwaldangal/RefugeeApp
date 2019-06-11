import urllib.request as urllib2
from lxml import etree
import io

url = "https://www.nytimes.com/"
response = io.StringIO( urllib2.urlopen(url))
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
search_link = tree.xpath("//*[@id=\"app\"]/div[2]/div/header/section[1]/div[1]/div[2]/button")[0]
print(search_link)
