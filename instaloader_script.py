import instaloader
import time
import random

# Initialize the Instaloader
L = instaloader.Instaloader()

# Log in to your Instagram account
L.interactive_login("YOUR_INSTAGRAM_USERNAME")
L.save_session_to_file()

# Get the profile
perfil = instaloader.Profile.from_username(L.context, "YOUR_INSTAGRAM_USERNAME")

# Delay function between requests
def delay():
    time.sleep(random.uniform(1, 3))

# Get the list of who you follow
L.context.log("Getting list of who you follow...")
following = {followee.username for followee in perfil.get_followees()}
delay()  # Delay after getting the full list

# Get the list of who follows you
L.context.log("Getting list of followers...")
followers = {follower.username for follower in perfil.get_followers()}
delay()  # Delay after getting the full list

# Find who is not following you back
not_following_back = following - followers

# Shows who is not following you back
print("People who are not following you back:")
for user in not_following_back:
    print(user)