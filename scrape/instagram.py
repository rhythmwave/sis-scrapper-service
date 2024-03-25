from rocketapi import InstagramAPI
from config import Config

config = Config()
rocket = InstagramAPI(token=config.ROCKET_TOKEN)

def scrape_instagram_profile(username):
    try:
        profile_data = rocket.get_user_info(username=username)
        return profile_data
    except Exception as e:
        raise Exception("Error scraping profile data: " + str(e))

def scrape_instagram_media(userid,count = config.INSTA_LIMIT):
    try:
        posts_data = rocket.get_user_media(userid,count)
        return posts_data
    except Exception as e:
        raise Exception("Error scraping reel data: " + str(e))
    
def scrape_instagram_comment(mediaid,count = config.INSTA_LIMIT):
    try:
        posts_data = rocket.get_media_comments(mediaid)
        return posts_data
    except Exception as e:
        raise Exception("Error scraping comments data: " + str(e))