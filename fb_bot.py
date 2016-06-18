#Author:Atul Kumar
#Date of creation:19/06/2016
#PACKAGE:facebook,facepy
#ABOUT:This script will comment and likes the post of particular fb page or user whose page_id or user_id is provided by user
#CAUTION:FB May detect that it's a bot and can block you..so go easy folks  lol!

import facebook,facepy

#Client Access token can be get at https://developers.facebook.com/tools
#Make sure you have checked checkbox labeled as publish_actions 
accessToken='' #Your Access Token here 

#Do query and fetch post_id of posts by page
graph0=facepy.GraphAPI(accessToken)
graph1=facebook.GraphAPI(access_token=accessToken,version='2.6')
victim_id=input("Enter the Victim facebook id: ")
query=victim_id+'/posts?fields=id&limit=50'
r=graph0.get(query)
postid=[x['id'] for x in r['data']]

print("There are %s post in list!"%len(postid))

choice=input("Do you want to post a comment on these posts? Y/N: ")
if choice=='Y':
	how_many_to_comment=int(input("On how many post you want to comment: "))
	if how_many_to_comment<=len(postid):
		comment=input("Enter the comment you want to post: ")
		for i in range(how_many_to_comment):
			tmp=postid[i]
			graph1.put_comment(object_id=tmp,message=comment) #Comment on post
			graph1.put_like(object_id=tmp) #Like the post
			print("Done commenting and liking on post %s"%(tmp))
		print("job done successfully!")
	else:
		print("Number of posts to comment exceeded!")
else:
	print("No worries,comment later!")
