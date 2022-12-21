import requests
import json
import re
import get_quote as quote
import get_likes as like
import get_retweet as retweet

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKxniQEAAAAAyi8SBUpu7BwlAXxQyBWkexkkDcE%3D4jaaFtAN5rPIFWyjs2p8GVNiLbYAzHSr0cPvtzPky6me8M0Xj3'


def extract_id_from_url(url):
  # Use a regular expression to find the number in the URL
  match = re.search(r'status/(\d+)', url)
  if match:
    # Return the number if it was found
    return match.group(1)
  else:
    # Return None if the number was not found
    return None

def main():
    # url = 'https://twitter.com/econ_jmp/status/1591336069508698112'
    url = 'https://twitter.com/SilviaG27358156/status/1603764199506706432'
    tweet_id = extract_id_from_url(url)
    # print(tweet_id)

    quote_count = quote.get_quote_number(tweet_id)
    print('quote', quote_count)

    like_count = like.get_like_count(tweet_id)

    print('like', like_count)

    retweet_count = retweet.get_retweet_count(tweet_id)

    print('retweet', retweet_count)



if __name__ == "__main__":
    main()
    
