import sys
sys.path.append('../src')
sys.path.append('src')

from scraper import IH_scraper


# Get a free token at www.influencerhunters.com
TOKEN = "XXXXXXXXXXXX"

#Initialize sender class 
scraper = IH_scraper(token_IH_API=TOKEN)

#Send the request to the IH server
print("sending the request, it might take few seconds..")
res, success = scraper.ig.get_user_posts_from_username(username="cristiano", depth=1, oldest_timestamp=1611308425 )


if success:
    print("Success!")
else:
    print("Something went wrong, check the response for more information. \n(Did you insert a valid token?)")
