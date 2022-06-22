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

## Start app
```bash
$ export LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
$ export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN
$ python app.py
```