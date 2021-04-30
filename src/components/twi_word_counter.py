# -*- coding:utf-8 -*-

# Web requests and parsers
import pickle
import requests
from bs4 import BeautifulSoup

# Importing sources, and chapter links
from components.indexer import get_chapter_links
from components.sources import getTWI

# Counter function, which counts the words
def counter(index):
    print("The Wandering Inn word counter")
    totalWordCount = 0
    chapter_number = 0
    print("Total Word Count Value : ", totalWordCount)
    for link in index:
        page = requests.get(link).text
        soup = BeautifulSoup(page, "html.parser")
        chapter_number += 1
        chapter_title = soup.find("h1", "entry-title")
        chapter_title = chapter_title.get_text()
        chapter_tag = soup.find("article", "post")
        text = chapter_tag.findChildren("p")
        text = text[:-1]
        text = str(text)
        text = text[1:-1]
        text = text.replace("<p>", "")
        text = text.replace("</p>,", "")
        text = text.replace("</p>", "")
        text = str(text)
        words = text.split()

        print(
            f"Chapter {chapter_number:<5} : {chapter_title:<40} | Word Count : {len(words)}"
        )
        totalWordCount += len(words)

        if chapter_number % 100 == 0:
            print(
                "Total Word Count till Chapter ",
                chapter_number,
                " is : ",
                totalWordCount,
            )

    print("Total Word Count : ", totalWordCount)
    print("Number of pages : ", totalWordCount / 450)


if __name__ == "__main__":
    novel_details = getTWI()
    links = get_chapter_links(novel_details["TableOfContents"])
    counter(links)
