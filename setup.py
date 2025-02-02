import os
import logging
import feedparser
from telegram import Bot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")  # Channel or group ID

# AI/ML/DS News RSS Feeds
RSS_FEEDS = [
    "https://ai.googleblog.com/feeds/posts/default",
    "https://feeds.feedburner.com/InsideBigData",
    "https://www.kdnuggets.com/feed",
    "https://towardsdatascience.com/feed",
]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

def fetch_latest_news():
    """Fetch latest articles from RSS feeds."""
    news_items = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:  # Fetch top 3 articles per feed
            news_items.append(f"\U0001F4F0 *{entry.title}*\n{entry.link}\n")
    return news_items

def send_news_updates():
    """Send news updates to Telegram channel/group."""
    news = fetch_latest_news()
    if not news:
        logging.info("No news found.")
        return
    for item in news:
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=item, parse_mode="Markdown")
        logging.info("News sent to Telegram.")

if __name__ == "__main__":
    send_news_updates()
