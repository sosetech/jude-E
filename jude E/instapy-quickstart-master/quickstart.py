
'''this program does the following
-follow people on a particular hashtag with less than 7000 followers
-unfollows people who dont follow after 5 days
-like and interact on peoples post using the hash tags
-likes posts on your feeds'''




# imports
from instapy import InstaPy
from instapy import smart_run
import random
# login credentials
insta_username = ''
insta_password = ''

# get a session!
session = InstaPy(username=insta_username, password=insta_password)


with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=2500,max_following=2200)

    #use the value of `False` to permanently turn it off
    session.set_simulation(enabled=False)
    
    session.set_user_interact(amount=2, randomize=True, percentage=75)
    session.set_do_follow(enabled=True, percentage=50)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(['#grandkid','#grandkids','#kids','#kid'],
                         amount=random.randint(30, 50), interact=True)
    
    session.follow_by_tags(['#grandkid','#grandkids','#kids','#kid'],
                         amount=random.randint(15, 25), interact=True) 
    
    session.unfollow_users(amount=random.randint(20, 35), instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=120*60*60, sleep_delay=600)
    
    session.like_by_feed(amount=random.randint(30, 45), randomize=True, interact=True)