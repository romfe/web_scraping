import requests
import subprocess
import optparse
from bs4 import BeautifulSoup

parser = optparse.OptionParser()
parser.add_option("-u","--url", dest = "url", help = "url of the website to be analyzed")
parser.add_option("-s", "--string", dest = "string", help = "string to search for on the page")
(options, arguments) = parser.parse_args()
url = options.url
string = options.string

print(url)
print(string)
if(url):
    print(True)
    
try:
    page = requests.get(url)
except:
    print("[-] Error accessing the website. Please verify the url and try again")
    exit()

rawHtml = BeautifulSoup(page.content, "html.parser")
print(rawHtml)