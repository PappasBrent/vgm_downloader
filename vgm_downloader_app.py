#!/usr/bin/python3
'''
A GUI for the VGM downloader
'''
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread

from vgm_downloader import VgmDownloader


class VGMDownloaderApp:
    '''
    Class for running the VGM downloader with a GUI
    '''

    def __init__(self, master):

        self.downloader = VgmDownloader()

        self.frame = ttk.Frame(master, padding=(15, 15))
        self.frame.pack()

        self.export_directory = StringVar(
            value='Please choose an export directory...')

        self.page_url = StringVar(value='Enter URL of OST page')

        self.label = ttk.Label(
            self.frame, text='VGM Downloader', justify=CENTER)
        self.label.config(font=("Courier", 18))
        self.label.grid(row=0, column=0, columnspan=2)

        self.entry_directory = ttk.Entry(self.frame, width=60,
                                         textvariable=self.export_directory)
        self.entry_directory.grid(row=1, column=0)

        ttk.Button(self.frame, text="Choose directory to save soundtrack to",
                   command=self.choose_directory).grid(row=1, column=1)

        self.entry_url = ttk.Entry(self.frame, width=60,
                                   textvariable=self.page_url)
        self.entry_url.grid(row=2, column=0)

        ttk.Button(self.frame, text='Download!',
                   command=self.start_download).grid(row=2, column=1)

    def choose_directory(self):
        '''
        Asks the user to set the export directory to save
        the chosen soundtrack in
        '''
        new_directory = filedialog.askdirectory()
        # Ensures that user selected a new directory
        if new_directory is not None:
            self.export_directory.set(new_directory)

    def start_download(self):
        '''
        Starts the downloads using the vgm_downloader module
        '''
        if not self.entry_url.get().startswith(self.downloader.prefix):
            messagebox.showerror("Invalid URL",
                                 "Please enter a valid KH Insider URL")
            return False

        directory_path = self.entry_directory.get()

        # Starts a new thread for the download so that the GUI doesn't freeze
        # Also allows for multiple soundtracks to be downloaded at once
        thread = Thread(target=self.downloader.download_all_mp3s,
                        args=(self.entry_url.get(), directory_path))
        thread.start()


def main():
    '''
    Executes script
    '''
    root = Tk()
    root.title("VGM Downloader")
    VGMDownloaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
