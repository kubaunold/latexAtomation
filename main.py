from urllib.request import urlretrieve
import urllib.request
from urllib.parse import quote, urlencode  #parsing text to url-compatile
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

fileName = "wl7.tex"

url_endpoint = "https://latexonline.cc/compile"
f = open(fileName, 'r', encoding="utf8") 
Lines = f.readlines() 
text=""
for line in Lines:
    text+=line
    # print("Line{}: {}".format(count, line.strip()))
qText = quote(text)
myDict = {'text': text, 'command':'pdflatex'}
# myDict2 = {'text': text, 'download': 'sample.pdf'}
url_rest = urlencode(myDict)
# print("qText: {}".format(qText))
# print("url_rest: {}".format(url_rest))
url = url_endpoint + "?" +  url_rest
print("url: {}".format(url))
# html = urlopen(url)
# print(html.read())
# contents = urlopen("http://example.com/foo/bar").read()


import requests
# url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
r = requests.get(url, stream=True)
with open('metadata.pdf', 'wb') as fd:
    for chunk in r.iter_content(100):
        fd.write(chunk)
print("DOne")