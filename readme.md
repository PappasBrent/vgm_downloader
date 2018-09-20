# KH Insider VGM Downloader

A simple and convenient way to download loads of sweet video game music with Python.

Version 1.0.0

## Table of Contents

- [KH Insider VGM Downloader](#kh-insider-vgm-downloader)
    - [Table of Contents](#table-of-contents)
    - [Getting Started](#getting-started)
        - [Prerequisites](#prerequisites)
        - [Installing](#installing)
    - [Built With](#built-with)
    - [Contributing](#contributing)
    - [Versioning](#versioning)
    - [Author](#author)
    - [License](#license)
    - [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

You're gonna need [Python](https://www.python.org/) (obviously).

More specifically, the modules in this package were made in Python 3.6.3
and updated to accomodate Python 3.7.0.
Any version of Python past 3 (i.e. 3.*) should work just as well though.

You will also need the Beautiful Soup 4. This wonderful web-scraping tool can be
easily installed from the command line with:
```
python -m pip install bs4
```
Granted that you have your preferred version of Python (remember, it should be 3.*)
added to your system path

### Installing

Simply download/clone this repo/package, unzip it, and run vgm_downloader_app.py.
This will launch the (hopefully) simple user interface application.

If you want to import the base downloader class for use in your
own projects, simply add this statement:

```python
import vgm_downloader
```

to the top of your Python program code and make sure that vgm_downloader.py
is in the same directory as your project.

## Built With

- [tkinter](https://docs.python.org/3/library/tk.html) - Module for GUI development
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Module for facilitating web scraping

## Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with me beforehand.

## Versioning

I'm using [SemVer](http://semver.org/) for versioning.

## Author

- **Brent Pappas** - *Initial work* - [Brent Pappas](http://www.pappasbrent.com)

## License

This project is licensed under the MIT License -
see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- My friend Josh D.
