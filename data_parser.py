from tkinter import filedialog
from tkinter import *

class DataParser():

    def __init__(self):
        pass

    def open_file_prompt(self):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir=".", title="Selecteer adressenbestand",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        self.fp = root.filename

    def open_file_path(self, filepath):
        self.fp = filepath