import time, os #stdlib
import tweepy, nltk #external libs
import database, sentiment_analyzer #libs we wrote
import pickle

bearer_token = os.environ['TWITTER_BEARER_TOKEN']

class STREAM_API(tweepy.StreamingClient):
    conn = database.connect()
    cur = conn.cursor()
    seen = 0
    def on_tweet(self, tweet):
        '''handle tweet; i.e. find sentiment, store in database'''
        self.seen+=1
        tweet_time = time.time() #note: tweet.created_at is None for some reason.
        print('new tweet at ',tweet_time)
        sentiment = sentiment_analyzer.find_sentiment(tweet.text)

        self.cur.execute("INSERT INTO tweets VALUES (?,?,?,?, ?,?,?,?,?)",
                        (None, tweet.id, tweet_time, tweet.text,
                        sentiment['overall'],
                        sentiment['neg'],
                        sentiment['neu'],
                        sentiment['pos'],
                        sentiment['compound']))

        if self.seen%50 == 0:
            #maybe don't thrash the disk?
            print('50 new tweets; saving to DB')
            self.conn.commit()

    def delete_all_rules(self):
        ''' clear all rules (stored twitter-side);
        max # of rules on 'Essential' twitter API access level is 5,
        so you must delete some or all rules to add others;
        https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level
        '''
        response=self.get_rules()
        rule_list = response.data
        if rule_list != None:
            ids = [rule.id for rule in rule_list]
            self.delete_rules(ids)

STREAM = STREAM_API(bearer_token = bearer_token)#,
#STREAM.delete_all_rules()

#NOTE: you can have max 5 rules with Essential API access
#however, each rule can have many terms, the below is ONE rule not 3, for example
#https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule

STREAM.add_rules([tweepy.StreamRule('bitcoin OR litecoin OR ethereum'),])

current_rules = STREAM.get_rules()
print('current rules: ',current_rules)

STREAM.filter()
