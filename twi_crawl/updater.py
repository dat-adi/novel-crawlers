import pickle
from indexer import get_chapter_links, set_chapter_file_links

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

if __name__ == "__main__":
    update_chapters()
