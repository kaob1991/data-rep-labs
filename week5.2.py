import requests
import urllib.parse
from config import tempgit as cnfg
import json


url = 'https://api.github.com/repos/kaob1991/testprivate'
apiKey = cnfg["githubpat"]
#api = "XXXXXXXX"
#apiurl = 'https://api.html2pdf.app/v1/generate'
#params = {'url': targetUrl,'apiKey': apiKey}
#parsedparams = urllib.parse.urlencode(params)
#requestUrl = apiurl +"?" + parsedparams
#response = requests.get(requestUrl)
#print (response.status_code)
#result =response.content
#with open("document2.pdf", "wb") as handler:
 #   handler.write(result)


response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print (response.json())
with open("gittest.json", 'w') as fp:
    json.dump(repoJSON, fp, indent=4)