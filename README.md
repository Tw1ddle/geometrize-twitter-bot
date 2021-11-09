[![Geometrize Twitter bot logo](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/logo.png?raw=true "Geometrize - geometrizing images into geometric primitives Twitter bot logo")](https://www.geometrize.co.uk/)

[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/LICENSE)
[![Geometrize Twitter Bot Build Status](https://ci.appveyor.com/api/projects/status/github/Tw1ddle/geometrize-twitter-bot)](https://ci.appveyor.com/project/Tw1ddle/geometrize-twitter-bot)

[Twitter bot](https://twitter.com/Geometrizer) for [Geometrize](https://www.geometrize.co.uk/), an app for geometrizing images into geometric primitives. The bot waits for images to be tweeted at it. It geometrizes images it receives into shapes, and [posts the results 
on Twitter](https://twitter.com/Geometrizer).

[![Geometrized Forest](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/forest.png?raw=true "Forest, 2000 circles")](https://www.geometrize.co.uk/)

## Usage

Tweet an image at the [bot](https://twitter.com/Geometrizer) for a random result:

```
@Geometrizer Hi, geometrize bot!
```

Or tweet the specific numbers of shapes you want the bot to use, in the order they should be added to the image:

```
@Geometrizer rotated_ellipses=50 circles=50 rotated_rectangles=100 triangles=30 - thanks Geometrize bot!
```

Here is an example of how it is done:

[![Example Geometrize Bot Tweet](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/example_geometrize_tweet.png?raw=true "Example Geometrize Tweet")](https://www.geometrize.co.uk/)

## Development

### Prerequisites

 * Get a copy of [Geometrize](https://www.geometrize.co.uk/). Install or copy it into the [geometrize](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/geometrize) subfolder.
 * Install Python 3.x, pip, and the tweepy and Pillow libraries.
 * A fresh Twitter app on the Twitter [apps dashboard](https://apps.twitter.com/).

### Setup

Fill in the Twitter app credentials in [config.py](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/bot/config.py) and then run the bot:

```
python bot.py
```

The bot should connect to the Twitter streaming API. Console output should look [like this](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/successful_startup.png?raw=true).

Tweet an image at the bot. After a few moments, the bot will tweet a geometrized version back at you.

## Notes
 * If you want to develop the bot further, take a look at the [documentation](https://botdocs.geometrize.co.uk/).
 * Got an idea or suggestion? Open an issue on GitHub, or send Sam a message on [Twitter](https://twitter.com/Sam_Twidale).
 * This bot was inspired by [primitive](https://github.com/fogleman/primitive), a Go library created by [Michael Fogleman](https://github.com/fogleman).