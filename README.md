[![Geometrize Twitter bot logo](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/logo.png?raw=true "Geometrize - geometrizing images into geometric primitives Twitter bot logo")](http://www.geometrize.co.uk/)

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/LICENSE)
[![Travis Twitter Bot Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot)
[![AppVeyor Twitter Bot Build Status](https://ci.appveyor.com/api/projects/status/e9d5ghphfm3oa2au?svg=true)](https://ci.appveyor.com/project/Tw1ddle/geometrize-twitter-bot)
[![Travis Twitter Bot Docs Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot-docs.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot-docs)

This is a [Twitter bot](https://twitter.com/Geometrizer) for [Geometrize](http://www.geometrize.co.uk/), a tool for geometrizing images into geometric primitives. It waits for images to be tweeted at it, geometrizes the images into shapes, and [posts the results 
on Twitter](https://twitter.com/Geometrizer).

[![Geometrized Old Man of Storr](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/old_man_of_storr.jpg?raw=true "Old Man of Storr, 400 triangles")](http://www.geometrize.co.uk/)

## Usage

Simply tweet an image at the [bot](https://twitter.com/Geometrizer):

```
@Geometrizer Hi, cool geometrize bot!
```

Tweet the specific numbers of shapes you want the bot to use, in the order they will be added to the image:

```
@Geometrizer 50 rectangles, 50 circles, 50 rotated rectangles, 20 triangles. Thanks geometrize bot!
```

## Development

### Prerequisites

 * A copy of [Geometrize](http://www.geometrize.co.uk/). Install or copy it into the [geometrize](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/geometrize) subfolder.
 * Python 3.x with pip, tweepy and Pillow libraries.

### Setup Steps

Fill in your Twitter app credentials in [config.py](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/bot/config.py), and run the bot:

```
python bot.py
```

The bot should connect to the Twitter streaming API with console output like this:

```
 ..|'''.|  '||''''|   ..|''||   '||    ||' '||''''|  |''||''| '||''|.   '||' |'''''||  '||''''|
.|'     '   ||  .    .|'    ||   |||  |||   ||  .       ||     ||   ||   ||      .|'    ||  .
||    ....  ||''|    ||      ||  |'|..'||   ||''|       ||     ||''|'    ||     ||      ||''|
'|.    ||   ||       '|.     ||  | '|' ||   ||          ||     ||   |.   ||   .|'       ||
 ''|...'|  .||.....|  ''|...|'  .|. | .||. .||.....|   .||.   .||.  '|' .||. ||......| .||.....|

+-+-+-+-+-+-+-+ +-+-+-+
|T|W|I|T|T|E|R| |B|O|T|
+-+-+-+-+-+-+-+ +-+-+-+

Running test to ensure Geometrize is working correctly...
Geometrize startup test succeeded!

Will create Geometrize bot
Will create Twitter stream listener
Did create Twitter stream listener
Did create Geometrize bot
Twitter stream listener did connect
```

Finally tweet an image at the bot. After a few moments, the bot will tweet the geometrized version back at you.

## Notes
 * If you want to develop the bot further, take a look at the [documentation](http://botdocs.geometrize.co.uk/).
 * Got an idea or suggestion? Open an issue on GitHub, or send Sam a message on [Twitter](https://twitter.com/Sam_Twidale).
 * This bot was inspired by [primitive](https://github.com/fogleman/primitive), a Go library created by [Michael Fogleman](https://github.com/fogleman).