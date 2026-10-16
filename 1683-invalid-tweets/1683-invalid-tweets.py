import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ans = tweets[tweets.content.str.len() > 15]
    return ans[['tweet_id']]