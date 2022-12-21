# import get_ids as id

import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


# def auth():
#     return os.environ.get("BEARER_TOKEN")
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKxniQEAAAAAyi8SBUpu7BwlAXxQyBWkexkkDcE%3D4jaaFtAN5rPIFWyjs2p8GVNiLbYAzHSr0cPvtzPky6me8M0Xj3'

def create_url(tweet_id):

    return "https://api.twitter.com/2/tweets/{}/quote_tweets".format(tweet_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld

    # return {"tweet.fields": "created_at"}
    return {"tweet.fields": "author_id", "max_results": 100, 'exclude': 'retweets'}



def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def get_quote_number(tweet_id):
    url = create_url(tweet_id)
    headers = create_headers(bearer_token)
    params = get_params()
    json_response = connect_to_endpoint(url, headers, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    quote_number = json_response['meta']['result_count']
    # print(quote_number)
    return quote_number





def main():
    # # Replace with Tweet ID below
    # tweet_id = '1592369991973601281' 
    # url = create_url(tweet_id)
    # headers = create_headers(bearer_token)
    # params = get_params()
    # json_response = connect_to_endpoint(url, headers, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    # quote_number = json_response['meta']['result_count']
    # print(quote_number)


    # tweet_id = '1591336069508698112'

    # quote_count = get_quote_number(tweet_id)

    # print(quote_count)
    pass





if __name__ == "__main__":
    main()
    