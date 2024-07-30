[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=Python&logoColor=yellow)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.10.0-3776AB?style=flat&logo=telegram&logoColor=white")](https://redis.io/)
# GroupChatIDBot

***This is a simple Telegram bot built using the aiogram library. 
The bot responds to any incoming message by echoing back the chat ID from which the message was sent. 
It’s a handy tool for quickly retrieving chat IDs in your Telegram chats.***

## Features

- Echoes back the chat ID of the sender.
- Logs received chat IDs and any errors encountered.

## Requirements

- Python 3.11 or higher
- Libraries:  aiogram, python-dotenv

## Installation

1. Clone the repository:
```sh
git clone https://github.com/dev-lymar/GroupChatIDBot.git
cd GroupChatIDBot
```
2. Create and activate a virtual environment (recommended but optional):
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install dependencies:
```sh
pip install -r requirements.txt
```
4. Create a `.env` file from the example:

*Then, open the .env file in a text editor and add your API token:*
```sh
API_TOKEN=your_telegram_bot_api_token
```
*Obtain your API_TOKEN by registering your bot with [BotFather](https://telegram.me/BotFather).*

## Running the Bot
1. Start the bot:
```sh
python check_id_bot.py
```
2. To stop the bot, use `Ctrl+C` (or `Cmd+C` on macOS) in the terminal.

## Logging

- Logs are output to the console and can be useful for debugging and monitoring the bot’s operation.
- To change the logging level, adjust the `level` parameter in `logging.basicConfig`.

## Notes

- This project was developed using [Python 3.12](https://www.python.org/).
- This bot is minimalistic and primarily serves to return chat IDs. It can be extended to perform additional tasks as needed.

## License

This project is licensed under the MIT License. 
See the LICENSE file for details.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. 
Contributions are welcome!