print("deepak")
TEMP =123
print (TEMP)
print(TEMP + TEMP)

from InstagramAPI import InstagramAPI

users_list = []
post_list = []

def get_likes_list(username):
    api.login()
    api.searchUsername(username)
    result = api.LastJson
    #print("username" +  result)
    username_id = result['user']['pk'] # Get user ID
    #print("user id" username_id)
    user_posts = api.getUserFeed(username_id) # Get user feed
    for post in user_posts: # Push users to list
        print(post)
        post_list.append(post)
    #print("Post" result)
    result = api.LastJson
    media_id = result['items'][0]['id'] # Get most recent post
    api.getMediaLikers(media_id) # Get users who liked
    users = api.LastJson['users']
    for user in users: # Push users to list
    #    print(user['username'])
        users_list.append({'pk':user['pk'], 'username':user['username']})


api = InstagramAPI("deepakpesu@gmail.com", "deshu321")
api.login()
get_likes_list("deepak")
