# line-bot-joy-english

# Prerequisite

## Use virtual env for developing
```bash
# Create a virtaul env 'linebot-env'
$ python -m venv linebot-env

# Activate the linebot-env for Linux or MacOS
$ source linebot-env/bin/activate

# For Windows
$ linebot-env\Scripts\activate.bat

# Install dependencies
$ pip install -r requirements.txt
```

## How to develop at local
```bash
# For MacOS or Linux
$ export LINE_CHANNEL_SECRET=<xxx>
$ export LINE_CHANNEL_ACCESS_TOKEN=ooo

# For Windows
$ set LINE_CHANNEL_SECRET=<xxx>
$ set LINE_CHANNEL_ACCESS_TOKEN=<ooo>

# Flask hot reload
$ export FLASK_DEBUG=1
$ set FLASK_DEBUG=1

# Point to our entry file
$ export FLASK_APP=app
$ set FLASK_APP=app

# Set the URI of Database
$ export DB_URI=<xxx>
$ set DB_URI=<xxx>

# Start our app
$ flask run

# Ngrok

$ ngrok http <port number>
```

# rich menu

[Using rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)

## Getting started

```
$ export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN
$ pip install -r requirements.txt
$ python rich-menu_app.py
```