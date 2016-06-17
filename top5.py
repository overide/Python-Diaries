#AUTHOR: Atul Kumar
#This script searches top 5 results of google search and open it in browser
#User can provide search term as command line argument or otherwise user will be prompted to supply search term!
#PACKAGES: Requests,BeautifulSoup(bs4)

import requests,webbrowser,bs4,sys

#Search Mechanism
def search(q):
	print("Googling...")
	res=requests.get(q)
	res.raise_for_status()
	print("Search Finished!!")

	soup=bs4.BeautifulSoup(res.text,"html.parser")
	result_links_list=soup.select('.r a')

	tabs_to_open=min(5,len(result_links_list))
	for i in range(tabs_to_open):
		webbrowser.open("https://www.google.com/"+result_links_list[i].get('href'))#Opening tabs in your default webbrowser

#Calling search() 
if len(sys.argv)>1:#If search term is provided as command line argument
	query="https://www.google.com/search?q="+" ".join(sys.argv[1:])
	try:
		search(query)
	except Exception as exp:
		print("An Error Occured: "+str(exp))
else:#Otherwise
	search_term=input("Enter your query: ")
	query="https://www.google.com/search?q="+search_term
	try:
		search(query)
	except Exception as exp:
		print("An Error Occured: "+str(exp))