## Twitter Sentiment Analyzer
*prototype 1 // December 23, 2022*

## OVERVIEW:
    This set of programs will monitor twitter for market sentiment.
    That means we can monitor a twitter stream for given terms, determine the sentiment of resulting tweets, store those tweets in a database, and query that database for recent sentiment (for now this is over the recent 500 tweets, but could be expanded to be a time window, e.g. 10 minute window or 30 minute window)

    to gather more tweets, run `twitter.py` (requires you first set up twitter API access / get a Bearer Token; free, takes a few minutes, see https://developer.twitter.com/en )

    to check market sentiment for the most recent 500 tweets, run `database.py`

    this works with the V2 API and the current v4+ tweepy library, so is current and doesn't rely on any deprecated API stuff; many stackoverflow type sites refer to out-of-date APIs specifically w/r/t twitter.

## Setup:
    You should run `pip install -r requirements.txt` and then `setup.py` to install the sentiment data.

## Files:
* `setup.py` - installs sentiment analyzer data (NLTK)
* `database.py` - database query functions (example: find overall sentiment for last 1000 tweets)
* `twitter.py` - twitter stream monitor (watch twitter, add tweets to db)
* `sentiment_analyzer.py` - analyze sentiment for a given string
* `sentiment.db` - a sample sqlite3 database pre-populated with a few thousand tweets

## Notes:
* tweets come in fast if monitoring big terms like "bitcoin", you will hit the API ratelimit.
* I think the best idea is to sample 1? minute of tweets every N minutes to gather market sentiment in order to avoid hitting the monthly limit of 500K tweets (increasable to 2 million if you upgrade your API access / that's also free)
* Maximum number of "rules" for twitter streaming is 5, but each "rule" can track many terms
* sentiment analyzer could be swapped for any number of others

## TODO / unhandled issues:
* this doesn't yet handle replies, retweets, etc in any special way
  * i.e. someone may be replying to a tweet about bitcoin with something about monero
  * i.e. you may be tracking the term "bitcoin" and get a hit for "dogecoin" and this will be because it was actually a reply to a bitcoin tweet.
* there is no throttling (other than rate limit handling which I believe tweepy handles automatically) 
  * i.e. there is nothing to stop you hitting the 500K/mo tweet limit
* currently there is only a "sentiment for last 1000 tweets" function,
* there is not yet a "sentiment for last 10 minutes" or any time-window thing
* also we are not separating tweets by their tracked phrase, e.g. we dont know if the tweet was for bitcoin or ethereum
* twitter seems to lock new developer accounts and make you re-verify a couple of times in the first week or so. A couple of times I got API errors only because they wanted the account re-verified. Just an FYI to help save you time.