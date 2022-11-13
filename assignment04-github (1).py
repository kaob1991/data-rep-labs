#Write a program in python that will read a file from a repository, 

#The program should then replace all the instances of the text "Andrew" with your name

#The program should then commit those changes and push the file back to the repository.

#I do not need to see your keys


from github import Github
from config import tempgit as pat
import requests


g = Github(pat["githubpat"])
search_text = "Andrew"
replace_text= "Katie"


#get repo clone url
repo = g.get_repo("kaob1991/-data-representation-coursework")
#print(repo.clone_url)

#get url of individual contents of git repo
fileInfo = repo.get_contents("sample.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Getting file content
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)


# using replace function to change Andrew to Katie 
new_contents = contentOfFile.replace(search_text,replace_text)


# Update file and push to repository
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
new_contents,fileInfo.sha)

print(gitHubResponse)