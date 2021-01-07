from indexer import get_chapter_links, set_chapter_file_links
from bs4 import BeautifulSoup
from components import download
import pickle
import requests

def offline_tester():
    try:
        link_list = get_chapter_links()
        set_chapter_file_links(link_list)
    except:
        with open("assets\\toc", "rb") as f:
            link_list = pickle.load(f)
            f.close()

def update_chapters():
    try:
        with open("assets\\toc", "rb") as f:
            links = pickle.load(f)
            f.close()
        link_list = get_chapter_links()
        if link_list != links:
            print("New chapters available")
            print("Updating chapters now...")
            set_chapter_file_links(link_list)
        else:
            print("Contents up to date")

    except FileNotFoundError as e:
        print("As file did not exist, we are currently creating the file...")
        set_chapter_file_links(get_chapter_links())
        print("File created. Run again.")
    except Exception as e:
        print(e)


def clean_children(file_name_in, file_name_out):
    raw = open(file_name_in, "r", encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")
    raw.close()
    chapter_tag = soup.find("article", "post")
    chapter_title = soup.find('h1', 'entry-title')
    chapter_title = chapter_title.get_text()
    text = chapter_tag.findChildren('p')
    text = text[:-1]
    text = str(text)
    text = text[1:-1]
    text = text.replace("</p>,", "</p>\n")
    f = open(file_name_out, "w", encoding="utf-8")
    f.write(
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: https://daisy.org/z3998/2012/vocab/structure/" lang="en" xml:lang="en">'
    )
    f.write("\n<head>")
    f.write("\n<title>" + chapter_title + "</title>")
    f.write("\n</head>")
    f.write('\n<body dir="default">')
    f.write("\n<h1>" + chapter_title + "</h1>")
    f.write(text)
    f.write("\n</body>")
    f.write("\n</html>")
    f.close()
    print(text)


def get_images(file_name_in):
    raw = open(file_name_in, "r", encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")
    raw.close()
    links = []
    image_tag = soup.find_all('img')
    for link in image_tag:
        links.append(link.get('src'))
    return links


def img_download(file_name, links):
    for link in links:
        response = requests.get(link)
        print(link)
        file = open(file_name, "wb")
        file.write(response.content)
        file.close()



if __name__ == "__main__":
    #clean_children("soup_tester.txt", "soup_output.xhtml")
    img_download("sample_image.png", (get_images("assets\\soup_output.xhtml")))
