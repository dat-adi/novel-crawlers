#!/usr/bin/python
# -*- coding: utf-8 -*-

# Brings in the ContentBuilder which builds the EPUB by connecting all the components
from components.scrapper import ContentBuilder
from components.sources import getNovelDetails

"""This piece of code acts as the hub for CLI users."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


def user_prompt():
    try:
        version_info = open("../assets/version.txt", "r").read()
        print("Novel Crawlers | " + version_info)
    except:
        print("Novel Crawlers | Version Unknown" )
    finally:
        print("...")
        print("1. The Wandering Inn, by pirateaba")
        print("2. Worm, by WildBowPig")
        novel_details = getNovelDetails(eval(input("> ")))

        output_folder = input("Enter the storage path : ")
        NovelBuilder = ContentBuilder(
            novel_details["ChapterName"],
            novel_details["NovelName"],
            novel_details["Author"],
            novel_details["TableOfContents"],
            output_folder
        )
        return NovelBuilder


if __name__ == "__main__":
    novel_selection = user_prompt()
    while True:
        print("You have picked ", novel_selection.NovelName, ", Are you sure?(y/n)")
        if input("> ") != "y":
            break
        novel_selection.web()
        print("Thank you for using Novel Crawlers!")
        print("Your book is now stored at the location ", novel_selection.OutputFolder)
        break

    print("Exiting...")
