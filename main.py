import json
followers = open(''' Address of followers.json provided by instagram on request ''')
following = open(''' Address of following.json provided by instagram on request ''')
  
followers_data = json.load(followers)
following_data = json.load(following)

follower_list=[]
following_list=[]


for i in followers_data['relationships_followers']:
    user_val=i["string_list_data"]
    u=user_val[0]
    follower_list.append(u["value"])
    

for i in following_data['relationships_following']:
    user_val=i["string_list_data"]
    u=user_val[0]
    following_list.append(u["value"])

folo_folin=list(set(follower_list)-set(following_list))
folin_folo=list(set(following_list)-set(follower_list))      

j=1
print("\n")
print("People who dont follow me back: ")
for i in folin_folo:
	print(str(j)+") "+i)
	j=j+1

j=1
print("\n")
print("People who I dont follow back: ")
for i in folo_folin:
	print(str(j)+") "+i)
	j=j+1

followers.close()
following.close()
