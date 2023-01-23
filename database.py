import sqlite3

def dict_factory(cursor, row):
    '''return sqlite db rows as python dicts'''
    d = {}
    for idx, col in enumerate(cursor.description):d[col[0]] = row[idx]
    return d

def connect():
    '''connect to sqlite db'''
    conn = sqlite3.connect('sentiment.db')
    conn.row_factory = dict_factory
    return conn

def find_recent_market_sentiment():
    conn = connect()
    cur = conn.cursor()
    rows = cur.execute(f'SELECT * FROM tweets ORDER BY id DESC LIMIT 500').fetchall()
    sentiment_values = [row['tweet_sentiment_overall'] for row in rows]
    result = sum(sentiment_values) / len(sentiment_values)
    print('market sentiment: ')
    return result

if __name__ == "__main__":
    find_recent_market_sentiment()