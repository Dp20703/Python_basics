import urllib
import urllib.request

sampleurl=urllib.request.urlopen("https://www.google.com/")
print("The result:" + str(sampleurl.getcode()))