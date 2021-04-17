# Novel Crawlers
Web crawlers built to get your light novel content from the web, to you.

### Features

- [x] Crawling the page and returning content
- [ ] Offering light novel options available in the site
- [ ] Downloading the light novels in different formats.

### Books
- [x] [The Wandering Inn](https://wanderinginn.com)
- [ ] [Worm](https://parahumans.wordpress.com)

### A little about novel-crawlers
The purpose for making this repository was for the convenience of being able to read the books on my phone offline, as I'm used to travelling a lot and mobile data is quite the issue.
Having found no epubs online for download, I've sought out to make this repository with a few python scripts to let me get my content.

I hold no power over the content, and all credit to the books and the amazing content inside them, should be given to the authors.\
So, please support them, as this is simply a project made for convenience and nothing else.

## Usage
The flow of utilization of novel crawlers is through the `scrapper.py`, which loads in all the components from the different python files and executes them generating us an EPUB file to use.
The `scrapper.py` creates a class for the Book and the web() function takes in the table of contents as the input and downloads the content in the form of `.xhtml` files.
These `.xhtml` files are then placed into a zip file along with a few other files creating an EPUB file.
These folders and files are,
 - mimetype => Used to identify what kind of file the reader is dealing with, application/epub+zip in this case.
 - container.xml => Creates a structure in the form of a container for the EPUB File.
 - Content.opf => Metadata.
 - toc.ncx => Table of Contents.

## License
This repository is hosted under the MIT License, and is available for use.
