import snscrape.modules.twitter as sntwitter

for i, tweet in enumerate(sntwitter.TwitterSearchScraper("Reliance stock").get_items()):
    if i > 5:
        break
    print(tweet.content)