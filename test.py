import unittest
from unittest.mock import patch, MagicMock
import feedparser
from telegram import Bot
from telegram.error import TelegramError
from bot import fetch_latest_news, send_news_updates

class TestTelegramBot(unittest.TestCase):
    
    @patch("bot.feedparser.parse")
    def test_fetch_latest_news(self, mock_parse):
        """Test fetching news from RSS feeds."""
        mock_parse.return_value = MagicMock(entries=[
            {"title": "Test Article 1", "link": "http://example.com/1"},
            {"title": "Test Article 2", "link": "http://example.com/2"},
        ])
        news = fetch_latest_news()
        self.assertEqual(len(news), 2)
        self.assertIn("Test Article 1", news[0])
        self.assertIn("http://example.com/1", news[0])
    
    @patch("bot.Bot.send_message")
    @patch("bot.fetch_latest_news")
    def test_send_news_updates(self, mock_fetch_news, mock_send_message):
        """Test sending news updates to Telegram channel."""
        mock_fetch_news.return_value = [
            "\U0001F4F0 *Test Article*\nhttp://example.com/news"
        ]
        send_news_updates()
        mock_send_message.assert_called_once()
        mock_send_message.assert_called_with(
            chat_id="YOUR_TELEGRAM_CHANNEL_ID",  
            text="\U0001F4F0 *Test Article*\nhttp://example.com/news",
            parse_mode="Markdown"
        )
    
    @patch("bot.Bot.send_message", side_effect=TelegramError("Failed to send"))
    def test_send_news_updates_failure(self, mock_send_message):
        """Test handling Telegram API errors gracefully."""
        with self.assertLogs(level='INFO') as log:
            send_news_updates()
            self.assertIn("Failed to send", log.output[0])

if __name__ == "__main__":
    unittest.main()
