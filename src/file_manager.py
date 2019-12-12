import os
import hashlib

"""
Function to manage all the reading of folder and files for the monitoring 
"""

sha256 = hashlib.sha256()
sha_list = []


def reading_folder():
    f_list = os.listdir()
    return f_list


def get_sha():
    list_ = reading_folder()
    for file in list_:
        print(file)
        print(sha256.hexdigest())
        sha_list.append(file.sha256.hexdigest())
    print(sha_list)
    return sha_list


get_sha()