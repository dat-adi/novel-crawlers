#!/usr/bin/python
# -*- coding: utf-8 -*-

# Brings in the ContentBuilder which builds the EPUB by connecting all the components
from components.scrapper import ContentBuilder
from components.sources import getTWI

'''This piece of code acts as the hub for CLI users.'''

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


def user_prompt():
    version_info = open("../assets/version.txt", "r").read()
    print("Novel Crawlers | " + version_info)
    print("...")
    print("1. The Wandering Inn, by pirateaba")
    print("2. Worm, by WildBowPig")
    ln_selection = int(input("> "))
    return ln_selection


if __name__ == "__main__":
    print(user_prompt())
