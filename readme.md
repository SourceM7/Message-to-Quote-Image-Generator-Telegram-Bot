# Message to Quote Image Generator Telegram Bot

A Telegram bot that generates images of quotes from messages within a group chat. The bot listens for mentions and then creates an image featuring the quoted message and the user who was mentioned.

## Features

- Automatically generate quote images from Telegram group messages.
- Customizable bot settings through simple configuration.
- Lightweight and easy to set up.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Contributing](#contributing)

## Installation

Follow these steps to set up and run the bot:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SourceM7/Message-to-Quote-Image-Generator-Telegram-Bot.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Message-to-Quote-Image-Generator-Telegram-Bot
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Ensure Google Chrome is installed on your system.** The bot uses Chrome for rendering images.

## Configuration

1. **Create and edit the `.env` file with the following content:**
    ```plaintext
    BOT_TOKEN=YOUR_BOT_TOKEN
    BOT_USERNAME=YOUR_BOT_USERNAME
    ```
    Replace `YOUR_BOT_TOKEN` and `YOUR_BOT_USERNAME` with your actual bot token and username.

## Running the Bot

1. **Ensure the `.env` file is set up correctly.**
2. **Run the bot:**
    ```bash
    python main.py
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
