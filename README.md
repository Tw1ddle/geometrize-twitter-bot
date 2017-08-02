[![Geometrize Twitter bot logo](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/logo.png?raw=true "Geometrize - geometrizing images into geometric primitives Twitter bot logo")](http://www.geometrize.co.uk/)

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/LICENSE)
[![Travis Twitter Bot Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot)
[![AppVeyor Twitter Bot Build Status](https://ci.appveyor.com/api/projects/status/TODO?svg=true)](https://ci.appveyor.com/project/Tw1ddle/geometrize-twitter-bot)

This is a [Twitter bot](https://twitter.com/Geometrizer) for [Geometrize](http://www.geometrize.co.uk/), a tool for geometrizing images into geometric primitives. It waits for images to be tweeted at it, geometrizes the images into shapes, and [posts the results 
on Twitter](https://twitter.com/Geometrizer).

[![Geometrized Old Man of Storr](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/old_man_of_storr.jpg?raw=true "Old Man of Storr, 400 triangles")](http://www.geometrize.co.uk/)

## Prerequisites

 * A copy of [Geometrize](http://www.geometrize.co.uk/). Install or copy it into the [geometrize](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/geometrize) subfolder.
 * Python 3.x with pip, tweepy and Pillow libraries.

## Usage

Download, fill in your Twitter app credentials in [config.py](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/bot/config.py), and run the bot:

```
python bot.py
```

It should connect to Twitter. Expect some output like this:

```
Will create Geometrize bot
Will create Twitter stream listener
Did create Twitter stream listener
Did create Geometrize bot
Stream listener did connect
```

Next, visit Twitter and tweet an image at the bot. After a few moments, the bot will tweet a geometrized version back at you (time taken may vary depending on how much of a backlog it has).

## Examples

Simply tweet an image at the bot:

```
@Geometrizer Hi, cool geometrize bot!
```

Tweet the specific numbers of shapes you want the bot to use, in the order they need to be added:

```
@Geometrizer 50 rectangles, 50 circles, 50 rotated rectangles, 20 triangles. Thanks geometrize bot!
```

## Notes
 * Got an idea or suggestion? Open an issue on GitHub, or send Sam a message on [Twitter](https://twitter.com/Sam_Twidale).
 * This bot was inspired by [primitive](https://github.com/fogleman/primitive), a Go library created by [Michael Fogleman](https://github.com/fogleman).