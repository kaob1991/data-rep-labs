import requests
import urllib.parse
from config import html2pdf as cnfg


targetUrl = "https://www.formula1.com/"
apiKey = cnfg["html2pdfkey"]
#api = "XXXXXXXX"
apiurl = 'https://api.html2pdf.app/v1/generate'
params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams
response = requests.get(requestUrl)
print (response.status_code)
result =response.content
with open("document2.pdf", "wb") as handler:
    handler.write(result)