import components
import zipfile
from indexer import get_chapter_links
import os


def web():
    info = {"ChapterName": "twi-", "NovelName": "Wandering Inn", "author": "pirateaba"}

    output_folder = input("Enter the output folder : ")

    link_list = get_chapter_links()

    file_list = []
    for x in range(len(link_list)):
        namer = link_list[x][36:-1]
        print(namer)
        '''
        # commented code below as intermediate files do not need to be redownloaded.
        components.download(link_list[x], os.path.join(output_folder, str(x) + ".html"))
        components.clean(
            os.path.join(output_folder, str(x) + ".html"),
            os.path.join(output_folder, info["ChapterName"] + str(namer) + ".xhtml"),
        )
        '''
        file_list.append(
            os.path.join(output_folder, info["ChapterName"] + str(namer) + ".xhtml")
        )
    components.generate(file_list, info["NovelName"], info["author"])


if __name__ == "__main__":
    web()
