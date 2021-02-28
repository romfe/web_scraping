import requests
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-u","--url", dest = "url", help = "url of the website to be analyzed")

(options, arguments) = parser.parse_args()
url = options.url
print(url)