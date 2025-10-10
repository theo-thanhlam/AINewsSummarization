from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-arts'

    fetchRSSToDatabase(cbcTopNews, topic_id=6,broadcaster_id=1)