from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-health'

    fetchRSSToDatabase(cbcTopNews, topic_id=5,broadcaster_id=1)