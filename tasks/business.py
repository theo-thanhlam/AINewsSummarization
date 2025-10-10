from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-business'

    fetchRSSToDatabase(cbcTopNews, topic_id=3,broadcaster_id=1)