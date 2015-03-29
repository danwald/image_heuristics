Image Heuristics
================

Image Hueristics is a REST API service to describe images.

Version
----

0.1

Tech
-----------

This blackbox [bottle](http://bottlepy.org/docs/dev/index.html) based service uses image processing tools provided by [OpenCV](http://opencv.org/), [Phash](http://www.phash.org/), [Pyssim](https://pypi.python.org/pypi/pyssim) to describe images them with verbs such as colored, noisy, blurry, over/under exposed and also provides a signature of an image of two types md5 and a perpetual hash which can be used to **GET** image description later on

Installation
--------------

This service utilises docker so you have to have docker installed. To run it locally you can ```docker pull danwald/image_heuristics``` 

Usage
-----
[WIP]
