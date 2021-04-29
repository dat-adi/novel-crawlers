# -*- coding:utf-8 -*-
# Accessing components
import components

# Zipfile creation modules
import zipfile

# Sources and Extractors
from components.indexer import get_chapter_links
from components.sources import getTWI

# Directory traversal
import os


# Builds the EPUB File
class ContentBuilder:
    # Defines output folder and book name
    def __init__(self, ChapterName, NovelName, Author):
        self.ChapterName = ChapterName
        self.NovelName = NovelName
        self.Author = Author

        self.OutputFolder = input("Enter the output folder : ")
        print(self.OutputFolder)


    # Generates the xhtml files
    def web(self, toc_link):
        info = {"ChapterName": self.ChapterName,"NovelName": self.NovelName, "author": self.Author}
        output_folder = self.OutputFolder

        link_list = get_chapter_links(toc_link)

        file_list = []
        for x in range(len(link_list)):
            namer = link_list[x][36:-1]
            print(namer)
            components.download(link_list[x], os.path.join(output_folder, str(x) + ".html"))
            components.clean(
                os.path.join(output_folder, str(x) + ".html"),
                os.path.join(output_folder, info["ChapterName"] + str(namer) + ".xhtml"),
            )
            file_list.append(
                os.path.join(output_folder, info["ChapterName"] + str(namer) + ".xhtml")
            )
        components.generate(file_list, info["NovelName"], info["author"])


if __name__ == "__main__":
    novel_details = getTWI()
    NovelBuilder = ContentBuilder(novel_details["ChapterName"], novel_details["NovelName"], novel_details["Author"])
