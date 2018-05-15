from tkinter import filedialog
from tkinter import *
import csv

class DataParser():

    def __init__(self, client):
        self.client = client

    def open_file_prompt(self):
        """
        Opens a prompt for selecting a .csv file. Works on Windows and Linux.
        :return:
        """
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir=".", title="Selecteer adressenbestand",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        self.fp = root.filename

    def open_file_path(self, filepath):
        """
        Reads the .csv filepath from a string
        :param filepath: Filepath to .csv file
        """
        self.fp = filepath

    def name_address_from_csv(self):
        """
        This function reads the address data from a .csv file and stores names-addresses as key-value pairs
        """
        self.address_list = {}

        with open(self.fp, 'r') as csvfile:
            raw_address_list = csv.reader(csvfile)
            for row in raw_address_list:
                name = row[0]
                address = row[1] + row[2] + row[3]
                geocode_result = self.client.geocode(address)
                data = {"address": address, "coords": geocode_result[0]['geometry']['location']}
                self.address_list[name] = data

        #print(self.address_list)