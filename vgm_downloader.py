#!/usr/bin/python3
'''
Downloads all mp3 file from a given KH Insider game soundtrack page
(because screw manually downloading each track one at at time)
'''

from os import chdir
import requests
from bs4 import BeautifulSoup

__author__ = "Brent Pappas"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Brent Pappas"
__email__ = "pappasbrent@gmail.com"
__status__ = "Production"


class VgmDownloader:
    '''
    Class for creating VGM Downloader objects
    '''

    def __init__(self):
        self.prefix = 'https://downloads.khinsider.com'

    def download_mp3(self, filename: str, url: str):
        '''
        Downloads an mp3 file from a given download page and saves it
        with a given filename
        (Note: This must be the actual download page i.e. the page that
        only contains the mp3 file itself)

        Args:
            filename:   The name to save the file as once downloaded
            url:        The url to download the mp3 file from
        '''
        with requests.get(url) as page:
            with open(f'{filename}', 'wb') as file:
                file.write(page.content)
        print("Download complete:", filename)

    def get_download_page_link(self, url: str):
        '''
        Returns the link to an mp3 file's download page
        from it's download preview page

        Args:
            url:    The url to the track's preview page.
                    The download link to the mp3 file of the track
                    can be found here.
        '''
        with requests.get(url) as page:
            soup = BeautifulSoup(page.content, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                if href.endswith('.mp3'):
                    return href

    def get_mp3_page_links(self, url: str):
        '''
        Gets the links to the download preview pages of each mp3 file

        Args:
            url:    The url to the soundtrack preview page.
                    A link to each track's preview page can be found here.
        '''
        with requests.get(url) as page:
            soup = BeautifulSoup(page.content, 'html.parser')
            # use a set comprehension instead of a list to avoid duplicates
            hrefs = {f"{self.prefix}{href}" for a in soup.find_all('a') if (
                href:= a.get('href')) and href.endswith('.mp3')}

            return list(sorted(hrefs))

    def download_all_mp3s(self, url: str, directory_path: str = None):
        '''
        Puts it all together

        Args:
            url:                The url to the soundtrack preview page
            directory_path:     The directory to download the soundtrack to.
                                If unspecified, then the directory that the
                                program was executed in will be used instead.

        Returns:
                                True if successful
        '''
        # Switch to designated directory if one was specified
        if directory_path is not None:
            chdir(directory_path)

        hrefs = self.get_mp3_page_links(url)

        for href in hrefs:
            # Only get the filename, not the whole link
            name = href[href.rfind('/') + 1:]
            # Replace special characters in links
            name = name.replace('%2520', '-').replace('%2528', '(').replace(
                '%2529', ')').replace('%2', ' ')

            download_link = self.get_download_page_link(href)

            self.download_mp3(name, download_link)

        print("All downloads complete")
        return True


def main():
    '''
    Executes script from command prompt
    '''
    print("Enter download link:")
    link = input()
    print("Enter download directory:")
    directory_path = input()
    downloader = VgmDownloader()
    downloader.download_all_mp3s(link, directory_path)


if __name__ == "__main__":
    main()
