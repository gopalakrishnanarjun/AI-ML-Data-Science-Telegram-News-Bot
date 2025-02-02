# AI& ML Data Science Telegram News Bot

This is a Telegram bot that fetches the latest news related to Artificial Intelligence (AI), Machine Learning (ML), and Data Science (DS) from various RSS feeds and posts them to a specified Telegram channel.

## Features
- Fetches news from top AI/ML/DS blogs and websites.
- Sends news updates directly to a Telegram channel or group.
- Uses RSS feeds to ensure up-to-date news.
- Can be scheduled to run automatically.

## Installation

### Prerequisites
- Python 3.8+
- A Telegram bot token (Get from [BotFather](https://t.me/BotFather))
- A Telegram channel/group ID

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/telegram-ai-news-bot.git
   cd telegram-ai-news-bot
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add:
   ```sh
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHANNEL_ID=your_channel_or_group_id_here
   ```
5. Run the bot:
   ```sh
   python bot.py
   ```

## Automation
To run this bot automatically at regular intervals, you can use:
- **Cron Jobs** (Linux/macOS)
- **Task Scheduler** (Windows)
- **APScheduler** (Python-based scheduling)

Example cron job (runs every 6 hours):
```
0 */6 * * * /usr/bin/python3 /path/to/bot.py
```

## Deployment
You can deploy this bot using:
- **GitHub Actions**
- **Heroku**
- **AWS Lambda**
- **Google Cloud Functions**

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License
This project is licensed under the MIT License.

---
