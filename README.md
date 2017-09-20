[![Geometrize Twitter bot logo](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/logo.png?raw=true "Geometrize - geometrizing images into geometric primitives Twitter bot logo")](http://www.geometrize.co.uk/)

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/LICENSE)
[![Travis Twitter Bot Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot)
[![AppVeyor Twitter Bot Build Status](https://ci.appveyor.com/api/projects/status/e9d5ghphfm3oa2au?svg=true)](https://ci.appveyor.com/project/Tw1ddle/geometrize-twitter-bot)
[![Travis Twitter Bot Docs Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot-docs.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot-docs)

[Twitter bot](https://twitter.com/Geometrizer) for [Geometrize](http://www.geometrize.co.uk/), an app for geometrizing images into geometric primitives. The bot waits for images to be tweeted at it. It geometrizes images it receives into shapes, and [posts the results 
on Twitter](https://twitter.com/Geometrizer).

[![Geometrized Forest](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/forest.png?raw=true "Forest, 2000 circles")](http://www.geometrize.co.uk/)

## Usage

Tweet an image at the [bot](https://twitter.com/Geometrizer) for a random result:

```
@Geometrizer Hi, geometrize bot!
```

Or tweet the specific numbers of shapes you want the bot to use, in the order they should be added to the image:

```
@Geometrizer 50 rotated ellipses, 50 circles, 50 rotated rectangles, 20 triangles. Thanks geometrize bot!
```

## Development

### Prerequisites

 * Get a copy of [Geometrize](http://www.geometrize.co.uk/). Install or copy it into the [geometrize](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/geometrize) subfolder.
 * Install Python 3.x, pip, and the tweepy and Pillow libraries.
 * A fresh Twitter app on the Twitter [apps dashboard](https://apps.twitter.com/).

### Setup

Fill in the Twitter app credentials in [config.py](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/bot/config.py) and then run the bot:

```
python bot.py
```

The bot should connect to the Twitter streaming API. Console output should look [like this](https://github.com/Tw1ddle/geometrize-twitter-bot/master/screenshots/forest.png).

Tweet an image at the bot. After a few moments, the bot will tweet a geometrized version back at you.

## Notes
 * If you want to develop the bot further, take a look at the [documentation](http://botdocs.geometrize.co.uk/).
 * Got an idea or suggestion? Open an issue on GitHub, or send Sam a message on [Twitter](https://twitter.com/Sam_Twidale).
 * This bot was inspired by [primitive](https://github.com/fogleman/primitive), a Go library created by [Michael Fogleman](https://github.com/fogleman).