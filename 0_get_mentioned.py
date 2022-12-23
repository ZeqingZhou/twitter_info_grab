import twitter_id as id
import twitter_mention as mention
import json

user_name = 'econ_jmp'

user_id = id.get_user_id(user_name)
mention_tweets = mention.get_tweets(user_id)
print(json.dumps(mention_tweets, indent=4, sort_keys=True))
