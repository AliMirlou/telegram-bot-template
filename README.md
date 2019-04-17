# Telegram Bot Template

A wrapper around `python-telegram-bot` (which is a wrapper itself :),
plus a user database on sqlite.

## How to use

First, install the prerequisites:

```bash
$ pip install -r requirements.txt
```

Then, write your command and message handler functions in `handlers.py` and
register them to the dispatcher in `dispatches.py`.

At last, change the `config.example.py` filename to `config.py` and
put your bot api token given by the BotFather as the value of `api_token` variable.

Then run `bot.py` to start your bot.

Note: This wrapper uses polling for now.
