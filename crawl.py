import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors(Allows you to play wwith Https sites)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask user to input weburl, parse it and Ignore ssl certificates
url = 'http://www.tinder.com'
html = urllib.request.urlopen(url,context=ctx).read() # file handle either loop through go line by line or read() once
soup = BeautifulSoup(html,'html.parser')

#Perform Anything you want to do!(kazlaw says feel free!)

itags = soup('img')
for tag_i in itags:
    print(tag_i.get('src',None)) # pull the links in the src attriibute

print('====================================================================')

print('|                                                                  |')
print('|                  <<<   ABOVE ARE MUWRP WEBSITE IMAGES     >>>    |')
print('|                                                                  |')
print('|                  <<<   BELOW ARE MUWRP WEBSITE LINKS      >>>    |')
print('|                                                                  |')

print('|                  <<<   KAZLAW @2021                       >>>    |')

print('====================================================================')

atags = soup('a')
for tag_a in atags:
    print(tag_a.get('href',None)) # pull the links in the href attribute