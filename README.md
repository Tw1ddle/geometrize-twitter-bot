[![Geometrize Twitter bot logo](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/logo.png?raw=true "Geometrize - geometrizing images into geometric primitives Twitter bot logo")](http://www.geometrize.co.uk/)

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/LICENSE)
[![Travis Twitter Bot Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot)
[![AppVeyor Twitter Bot Build Status](https://ci.appveyor.com/api/projects/status/TODO?svg=true)](https://ci.appveyor.com/project/Tw1ddle/geometrize-twitter-bot)

Work in progress.

This is a [Twitter bot](https://twitter.com/Geometrizer) for [Geometrize](http://www.geometrize.co.uk/), a tool for geometrizing images into geometric primitives. It takes any images tweeted at it, geometrizes them into shapes, and posts the results 
on Twitter.

[![Geometrized Astronaut](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/steve_smith_repairs_hubble.jpg?raw=true "Steve Smith repairs the hubble, 400 rotated rectangles, 100 rotated ellipses")](https://github.com/Tw1ddle/geometrize-lib)

## Prerequisites

 * A copy of [Geometrize](http://www.geometrize.co.uk/). Either install or copy it into the [geometrize](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/geometrize) subfolder.
 * An installation of Python 3.x and the pip, tweepy and Pillow libraries.

## Usage

Fill in your app credentials in [config.py](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/bot/config.py), and run the bot:

```
python bot.py
```

It should connect to Twitter, with output like this:

```
```

Once running, go on Twitter and tweet an image at the bot. After a few moments, the bot will tweet the corresponding geometrized image back at you (dependent on whether it has a backlog, of course).

## Examples

Simply tweet an image at the bot and it will Geometrize it:

```
@Geometrizer Hi, I like your bot!
```

Also can tweet the shapes you want the bot to use, in the order they should be added:

```
@Geometrizer 50 rectangles, 50 circles, 50 rotated rectangles, 20 triangles
```

## Notes
 * Got an idea or suggestion? Open an issue on GitHub, or send Sam a message on [Twitter](https://twitter.com/Sam_Twidale).
 * This bot was inspired by [primitive](https://github.com/fogleman/primitive), a Go library created by [Michael Fogleman](https://github.com/fogleman).