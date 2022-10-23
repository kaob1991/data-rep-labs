from github import Github
from config import tempgit as pat
import requests


g = Github(pat["githubpat"])


# Sanity check
#print("all okay")
# get all repo names
#for repo in g.get_user().get_repos():
 #   print(repo.name)

#get repo clone url
repo = g.get_repo("kaob1991/testprivate")
#print(repo.clone_url)

#get url of individual contents of git repo
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Contents of github file
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

#updating file with file contents
#newContents = contentOfFile + " more stuff \n"
#print (newContents)


#gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
#newContents,fileInfo.sha)

#print(gitHubResponse)
