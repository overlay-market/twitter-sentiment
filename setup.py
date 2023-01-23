import sqlite3, nltk

def create_sentiment_database():
    conn = sqlite3.connect("sentiment.db")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE tweets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tweet_id INTEGER,
            tweet_time INTEGER,
            tweet_text TEXT,
            tweet_sentiment_overall REAL,
            tweet_sentiment_neg REAL,
            tweet_sentiment_neu REAL,
            tweet_sentiment_pos REAL,
            tweet_sentiment_compound REAL)
        """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #create_sentiment_database() #sample database already included, so no need
    nltk.download('vader_lexicon')