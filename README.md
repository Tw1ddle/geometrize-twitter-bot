[![Geometrize Twitter bot logo](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/logo.png?raw=true "Geometrize - geometrizing images into geometric primitives Twitter bot logo")](http://www.geometrize.co.uk/)

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/LICENSE)
[![Travis Twitter Bot Build Status](https://img.shields.io/travis/Tw1ddle/geometrize-twitter-bot.svg?style=flat-square)](https://travis-ci.org/Tw1ddle/geometrize-twitter-bot)
[![AppVeyor Twitter Bot Build Status](https://ci.appveyor.com/api/projects/status/TODO?svg=true)](https://ci.appveyor.com/project/Tw1ddle/geometrize-twitter-bot)

This is a Twitter bot for [Geometrize](http://www.geometrize.co.uk/), a tool for geometrizing images into geometric primitives. It takes images tweeted at it, geometrizes them into shapes, and posts the results 
on Twitter.

[![Geometrized Astronaut](https://github.com/Tw1ddle/geometrize-twitter-bot/blob/master/screenshots/steve_smith_repairs_hubble.jpg?raw=true "Steve Smith repairs the hubble, 400 rotated rectangles, 100 rotated ellipses")](https://github.com/Tw1ddle/geometrize-lib)

## Prerequisites

 * A copy of [Geometrize](http://www.geometrize.co.uk/) and place it in the "geometrize" folder.
 * Python 3.x, pip, tweepy and Pillow.

## Usage

Fill in your app credentials in config.py, and run the bot:

''''

Once running, try tweeting an image at the bot. After a few seconds, the bot will tweet the corresponding geometrized image back at you.

You can tweet the desired shapes too.

''''

## Notes
 * Got an idea or suggestion? Open an issue on GitHub, or send Sam a message on [Twitter](https://twitter.com/Sam_Twidale).
 * This bot was inspired by [primitive](https://github.com/fogleman/primitive), a Go library created by [Michael Fogleman](https://github.com/fogleman).