# This was a quick project. Inspired by a story I heard of on the news where a guy did something almost exactly the same
#  and won a bunch of stuff. I couldn't find the code that that guy used (I don't think he wanted to release it), so I
# wrote this. Have fun.

import tweepy, time

#enter the corresponding information from your Twitter application:

CONSUMER_KEY = '8eflm2zA6ZloykrnMpdhtM1mJ' #keep the quotes, enter your consumer key
CONSUMER_SECRET = 'ATJwg9C2g0qQdwl7ls1zwjgFQY56WLf7vDUPUeIdUMTAI56SWV'#keep the quotes, enter your consumer secret key
ACCESS_KEY = '970520272318038016-i5NRGdXkN57VJbQGksRYUzFv2f9xHE1'#keep the quotes, enter your access token
ACCESS_SECRET =  'g8xJwTvdLGkn92xUo1E2F4EGpDnhxe7OtOdArQ6qZ78Jm'#keep the quotes, enter your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
keywords = ["rt to", "rt and win", "retweet and win", "rt for", "rt 4", "retweet to"]

bannedwords = ["vote", "bot", "b0t"]

bannedusers = ['bot', 'spot', 'lvbroadcasting'] # does not need to be the entire username! you can just put 'bot' for names like 'b0tspotter', etc.

def is_user_bot_hunter(username):
	clean_username = username.replace("0", "o")
	clean_username = clean_username.lower()
	for i in bannedusers:
		if i in clean_username:
			return True
		else:
			return False

def search(twts):
	for i in twts:
		if not any(k in i.text.lower() for k in keywords) or any(k in i.text.lower() for k in bannedwords):
			continue
		if is_user_bot_hunter(str(i.author.screen_name)) == False:
			if not i.retweeted:
				try:
					api.retweet(i.id)
					print ("rt " + (i.text))
					
					# huge thanks to github user andrewkerr5 for providing the fix for hashtags
					if "follow" in i.text or "#follow" in i.text or "Follow" in i.text or "#Follow" in i.text or "FOLLOW" in i.text or "#FOLLOW" in i.text or "following" in i.text or "#following" in i.text or "FOLLOWING" in i.text or "#FOLLOWING" or "Following" in i.text or "#Following" in i.text:
						user_id = i.retweeted_status.user.id
						api.create_friendship(user_id)

				except Exception:
					pass
				
			if ("fav" in i.text or "Fav" in i.text or "FAV" in i.text) and not i.favorited:
				try:
					api.create_favorite(i.id)
					print ("fav " + (i.text))
				except Exception:
					pass
			



def run():
	for key in ["RT to win", "retweet to win"]:
		print ("\nSearching again\n")
		search(api.search(q=key))


if __name__ == '__main__':
	while True:
		run()
