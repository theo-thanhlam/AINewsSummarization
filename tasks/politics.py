from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-politics'

    fetchRSSToDatabase(cbcTopNews, topic_id=4,broadcaster_id=1)