import urllib3
import requests
import time
import os

# List all indexes of the articles you need in the text file
files= open("list_of_ids.txt","r")

# Forms a list of all indices
list = [] 
for id in files:
	id=id.strip()
	list.append(id) 

files.close()

# Downloading Files
for i in range (len(list)):

	# To prevent time out when downloading lot of files
	time.sleep(20)	

	# Forming URL of the file
	url='https://'+'arxiv.org/pdf/'+list[i]+'.pdf'

	# Downloading file from arxiv.org & save file
	r = requests.get(url, stream = True)
	filename= list[i]+".pdf"
	os.chdir('/home/avinab/Desktop/Arxiv Scraper/Downloads/')
	with open(filename,"wb") as pdf:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				pdf.write(chunk)
	print("Downloaded {0} / {1} files".format(i+1,len(list)))
