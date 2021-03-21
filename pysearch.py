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

if(not url):
    print("[-] Please inform the url with the flag -u")
    exit()
elif(("http://" not in url) and ("https://" not in url)):
    print("[-] Please include either http:// or https:// in the provided url")
    exit()


if(not string):
    print("[-] Please inform the search string with the flag -s")
    exit()
    
try:
    page = requests.get(url)
except:
    print("[-] Error accessing the website. Please verify the url and try again")
    exit()

print("[+] All set, beginning search...")
rawHtml = BeautifulSoup(page.content, "html.parser")
print(rawHtml)