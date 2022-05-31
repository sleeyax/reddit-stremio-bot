# StremioBotUnofficial
This bot redirects users from r/Stremio to r/StremioAddons whenever a specific matching keyword is detected in a post. 

## Setup & deploy
From source:

```bash
# copy and modify praw config accordingly (see https://praw.readthedocs.io/en/stable/getting_started/configuration/prawini.html)
$ cp praw.ini.example praw.ini
# install dependencies
$ pip install -r requirements.txt
# run the bot
$ python bot.py
```

Docker:

```bash
$ docker build . -t stremio-bot-unofficial
$ docker run stremio-bot-unofficial
```

Kubernetes (modify `kubernetes.yaml` to suit your cluster setup first!)
```bash
$ kubectl apply -f kubernetes.yaml
```
