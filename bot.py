import praw
import time

reddit = praw.Reddit('bot1')
retrySecs = 1
maxRetrySecs = 300 # max 5 minutes
sub = reddit.subreddit('Stremio')


def handle_submission(submission):
    submission.reply("""This subreddit for Stremio application issues and feature requests. 
    For community built addon discussions please use: https://www.reddit.com/r/StremioAddons/
    
    This is an automated reply. If this is a false positive, please ignore (sorry).""")
    retrySecs = 1

def run():
    print("Watching for noobs...")
    for submission in sub.stream.submissions(skip_existing=True):
        needles = ["addon", "add on", "add-on", "plugin",
                   "plugins", "extension", "extensions"]
        if any(needle in submission.title.lower() for needle in needles) or any(needle in submission.selftext.lower() for needle in needles):
            handle_submission(submission)


try:
    while True:
        try:
            run()
        except Exception as e:
            print("Error: " + str(e))
            print("Trying again after {} seconds...".format(retrySecs))
            retrySecs = retrySecs * 2
            if retrySecs >= 300:
                retrySecs = 1
            time.sleep(retrySecs)
            pass
except KeyboardInterrupt:
    print("Exit.")
