from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-world'

    fetchRSSToDatabase(cbcTopNews, topic_id=2)