from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-technology'

    fetchRSSToDatabase(cbcTopNews, topic_id=7,broadcaster_id=1)