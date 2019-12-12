import os
import hashlib
import datetime

from src.database.connection import add_directory

"""
Function to manage all the reading of folder and files for the monitoring 
"""

sha256 = hashlib.sha256()
sha_list = []


def reading_folder():
    f_list = os.listdir()
    return f_list


def save_directory():
    list_ = reading_folder()
    print(list_)
    for file in list_:
        add_directory(datetime.datetime.now(), file, sha256.hexdigest)
        sha_list.append(file.sha256.hexdigest())
    return sha_list


save_directory()
