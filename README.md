![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)


# Twitter Bot

A Twitter Bot located at <a href="twitter.com/dirtOnMars"><b>@dirtOnMars</b></a> on Twitter. It uses a NASA API to post photos from the Mars Curiosity Rover every 15 minutes.

## Disclaimer

I hold no liability for what you do with this bot or what happens to you by using this bot. Abusing this bot *can* get you banned from Twitter, so make sure to read up on [proper usage](https://support.twitter.com/articles/76915-automation-rules-and-best-practices) of the Twitter API.

## Dependencies

You will need to install Python's [python-twitter](https://github.com/sixohsix/twitter/) library:

    pip install twitter

You will also need to create an app account on https://dev.twitter.com/apps

1. Sign in with your Twitter account
2. Create a new app account
3. Modify the settings for that app account to allow read & write
4. Generate a new OAuth token with those permissions

Following these steps will create 4 tokens that you will need to place in the configuration file discussed below.

## Usage

### Configuring the bot

Before running the bot, you must first set it up so it can connect to the Twitter API. Create a config.py file and import twitter. Create a function that returns the API using the four tokens you recieved from your Twitter Developer account.
      
    import twitter
		
		def getApi():
    return twitter.Api(consumer_key='yb33hvkIjNKu741ATZOj2LSEm',
                        consumer_secret='oFtlrhM723Yob7Spf4HOMRJyRFgMhdg2FU1yTnh5L8Hq1xpfLo',
                        access_token_key='1338233546172676098-V7FEIfTIz9w3NerLxS8LIVjTVqpKaW',
                        access_token_secret='Zljyyhm8GjM1SnOwAZ8wmXv9WNkcbb6XA4AvjobumAgdR')


### Create an instance of the bot

To create an instance of the bot. create a file called bot.py:

    import os
		from config import getApi
    
    api = getApi()

To test that your connection to Twitter is wortking, try running this simple status update function.
	#

  
    
## Have questions? Need help with the bot?

If you're having issues with or have questions about the bot, (https://github.com/BriaWilliams/twitterBot/issues) in this repository so one of the project managers can get back to you. 

