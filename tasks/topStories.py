from utils import fetchRSSToDatabase


if __name__ == "__main__":
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-topstories'

    fetchRSSToDatabase(cbcTopNews, topic_id=1,broadcaster_id=1)