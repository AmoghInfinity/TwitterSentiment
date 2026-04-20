import asyncio
import os
from dotenv import load_dotenv
from twikit import Client

load_dotenv()

async def main():
    client = Client()

    username = os.getenv("TWITTER_USERNAME")
    email = os.getenv("TWITTER_EMAIL")
    password = os.getenv("TWITTER_PASSWORD")

    await client.login(
        auth_info_1=username,
        auth_info_2=email,
        password=password
    )

    tweets = await client.search_tweet("Reliance stock", "Latest")

    for i, tweet in enumerate(tweets):
        if i > 5:
            break
        print(tweet.text)

asyncio.run(main())